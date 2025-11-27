import pygame
import sys
import time

# Inicialización de pygame
pygame.init()
ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Geometry Dash Básico")
reloj = pygame.time.Clock()

# Colores
NEGRO = (0, 0, 0)
AMARILLO = (255, 255, 0)
AZUL = (100, 100, 255)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
MORADO = (200, 100, 200)

# Constantes del juego
SUELO_Y = ALTO - 50  # Posición Y del suelo

# Clase 1: Jugador
class Jugador:
    def __init__(self):
        self.tamaño = 40
        self.x = 100
        self.y = SUELO_Y - self.tamaño
        self.velocidad_y = 0
        self.gravedad = 0.9  # Gravedad similar al Geometry Dash original
        self.fuerza_salto = -12  # Fuerza de salto ajustada
        self.en_suelo = True
    
    def saltar(self):
        if self.en_suelo:
            self.velocidad_y = self.fuerza_salto
            self.en_suelo = False
    
    def actualizar(self, obstaculos=None):
        self.velocidad_y += self.gravedad
        self.y += self.velocidad_y
        
        # Verificar si está en el suelo o en una plataforma
        self.en_suelo = False
        
        # Primero verificar si está en el suelo
        if self.y >= SUELO_Y - self.tamaño:
            self.y = SUELO_Y - self.tamaño
            self.velocidad_y = 0
            self.en_suelo = True
        
        # Luego verificar si está sobre algún obstáculo (plataforma)
        if obstaculos:
            for obstaculo in obstaculos:
                # Solo los bloques pueden servir como plataformas
                if isinstance(obstaculo, Bloque):
                    rect_jugador = self.obtener_rectangulo()
                    rect_obstaculo = obstaculo.obtener_rectangulo()
                    
                    # Verificar si el jugador está cayendo y está encima del obstáculo
                    if (self.velocidad_y >= 0 and 
                        rect_jugador.bottom >= rect_obstaculo.top and
                        rect_jugador.bottom - self.velocidad_y <= rect_obstaculo.top and
                        rect_jugador.right > rect_obstaculo.left and
                        rect_jugador.left < rect_obstaculo.right):
                        
                        self.y = rect_obstaculo.top - self.tamaño
                        self.velocidad_y = 0
                        self.en_suelo = True
    
    def dibujar(self, pantalla):
        pygame.draw.rect(pantalla, AMARILLO, (self.x, self.y, self.tamaño, self.tamaño))
    
    def obtener_rectangulo(self):
        return pygame.Rect(self.x, self.y, self.tamaño, self.tamaño)

# Clase 2: Obstáculo (Clase Padre)
class Obstaculo:
    def __init__(self, x, y, ancho, alto):
        self.x = x
        self.y = y
        self.ancho = ancho
        self.alto = alto
        self.velocidad = 6
    
    def actualizar(self):
        self.x -= self.velocidad
    
    def dibujar(self, pantalla):
        pass  # Las clases hijas implementarán esto
    
    def obtener_rectangulo(self):
        return pygame.Rect(self.x, self.y, self.ancho, self.alto)
    
    def esta_fuera(self):
        return self.x < -50

# Clase 3: Pincho (Hereda de Obstáculo)
class Pincho(Obstaculo):
    def __init__(self, x, ancho=30, alto=40):
        # Los pinchos siempre están sobre el suelo
        y = SUELO_Y - alto
        super().__init__(x, y, ancho, alto)
        self.color = MORADO
    
    def dibujar(self, pantalla):
        # Dibujar triángulo (pincho)
        punto1 = (self.x, self.y + self.alto)
        punto2 = (self.x + self.ancho, self.y + self.alto)
        punto3 = (self.x + self.ancho / 2, self.y)
        pygame.draw.polygon(pantalla, self.color, [punto1, punto2, punto3])

# Clase 4: Bloque (Hereda de Obstáculo)
class Bloque(Obstaculo):
    def __init__(self, x, ancho=50, alto=30):
        # Los bloques están sobre el suelo
        y = SUELO_Y - alto
        super().__init__(x, y, ancho, alto)
        self.color = ROJO
    
    def dibujar(self, pantalla):
        pygame.draw.rect(pantalla, self.color, (self.x, self.y, self.ancho, self.alto))

# Clase 5: Nivel
class Nivel:
    def __init__(self, numero, color_fondo, velocidad=6):
        self.numero = numero
        self.color_fondo = color_fondo
        self.velocidad = velocidad
        self.obstaculos = []
        self.crear_obstaculos()
    
    def crear_obstaculos(self):
        if self.numero == 1:
            # Nivel 1: Solo pinchos
            posiciones = [500, 800, 1100, 1400, 1700, 2000]
            for x in posiciones:
                self.obstaculos.append(Pincho(x))
        
        elif self.numero == 2:
            # Nivel 2: Más largo, bien espaciado y jugable
            # SECCIÓN 1: Introducción con pinchos simples
            self.obstaculos.append(Pincho(400))
            self.obstaculos.append(Pincho(550))
            
            # SECCIÓN 2: Primera plataforma y pinchos
            self.obstaculos.append(Bloque(750, 120, 25))
            self.obstaculos.append(Pincho(950))
            self.obstaculos.append(Pincho(1100))
            
            # SECCIÓN 3: Patrón de tres pinchos
            self.obstaculos.append(Pincho(1300))
            self.obstaculos.append(Pincho(1450))
            self.obstaculos.append(Pincho(1600))
            
            # SECCIÓN 4: Plataformas en escalera ascendente
            self.obstaculos.append(Bloque(1800, 80, 40))
            self.obstaculos.append(Bloque(1920, 80, 60))
            self.obstaculos.append(Bloque(2040, 80, 80))
            
            # SECCIÓN 5: Pinchos después de la escalera
            self.obstaculos.append(Pincho(2200))
            self.obstaculos.append(Pincho(2350))
            
            # SECCIÓN 6: Plataforma larga con pincho en medio
            self.obstaculos.append(Bloque(2550, 200, 30))
            self.obstaculos.append(Pincho(2650))
            
            # SECCIÓN 7: Escalera descendente
            alturas_descendentes = [100, 80, 60, 40, 20]
            for i, altura in enumerate(alturas_descendentes):
                self.obstaculos.append(Bloque(2850 + i * 70, 60, altura))
            
            # SECCIÓN 8: Patrón de pinchos final
            self.obstaculos.append(Pincho(3250))
            self.obstaculos.append(Pincho(3400))
            self.obstaculos.append(Pincho(3550))
            self.obstaculos.append(Pincho(3700))
            
            # SECCIÓN 9: Última plataforma y pincho final
            self.obstaculos.append(Bloque(3900, 150, 35))
            self.obstaculos.append(Pincho(4100))
            
            # SECCIÓN 10: Gran salto final
            self.obstaculos.append(Bloque(4300, 100, 50))
            self.obstaculos.append(Pincho(4500))
        
        elif self.numero == 3:
            # Nivel 3: Más obstáculos
            posiciones_pinchos = [300, 450, 600, 800, 950, 1100, 1300, 1500]
            posiciones_bloques = [350, 650, 900, 1200, 1400]
            
            for x in posiciones_pinchos:
                self.obstaculos.append(Pincho(x))
            
            for x in posiciones_bloques:
                self.obstaculos.append(Bloque(x))
    
    def actualizar(self):
        for obstaculo in self.obstaculos[:]:
            obstaculo.velocidad = self.velocidad
            obstaculo.actualizar()
            if obstaculo.esta_fuera():
                self.obstaculos.remove(obstaculo)
    
    def dibujar(self, pantalla):
        # Dibujar fondo
        pantalla.fill(self.color_fondo)
        
        # Dibujar suelo
        pygame.draw.rect(pantalla, AZUL, (0, SUELO_Y, ANCHO, 50))
        
        # Dibujar obstáculos
        for obstaculo in self.obstaculos:
            obstaculo.dibujar(pantalla)
    
    def verificar_colision(self, jugador):
        rect_jugador = jugador.obtener_rectangulo()
        for obstaculo in self.obstaculos:
            if rect_jugador.colliderect(obstaculo.obtener_rectangulo()):
                # Para bloques, solo cuenta como colisión si el jugador choca por los lados o desde abajo
                if isinstance(obstaculo, Bloque):
                    # Si el jugador está cayendo y aterriza encima, no es colisión
                    if (jugador.velocidad_y >= 0 and 
                        rect_jugador.bottom >= obstaculo.y and
                        rect_jugador.bottom - jugador.velocidad_y <= obstaculo.y):
                        continue  # No es colisión, es un aterrizaje
                return True
        return False
    
    def esta_completado(self):
        return len(self.obstaculos) == 0

# Clase 6: Juego (Controla el estado del juego)
class Juego:
    def __init__(self):
        self.estado = "menu"
        self.nivel_actual = 1
        self.jugador = Jugador()
        self.niveles = {
            1: Nivel(1, (50, 50, 150), 6),
            2: Nivel(2, (150, 50, 50), 7),
            3: Nivel(3, (50, 150, 50), 8)
        }
    
    def cambiar_estado(self, nuevo_estado):
        self.estado = nuevo_estado
    
    def cambiar_nivel(self, numero_nivel):
        self.nivel_actual = numero_nivel
        self.jugador = Jugador()  # Reiniciar jugador
    
    def obtener_nivel_actual(self):
        return self.niveles[self.nivel_actual]
    
    def reiniciar_nivel(self):
        self.niveles[self.nivel_actual] = Nivel(
            self.nivel_actual,
            self.niveles[self.nivel_actual].color_fondo,
            self.niveles[self.nivel_actual].velocidad
        )
        self.jugador = Jugador()

# Clase 7: Menu
class Menu:
    def __init__(self):
        self.botones = []
    
    def dibujar_menu_principal(self, pantalla):
        pantalla.fill(NEGRO)
        
        # Título
        fuente = pygame.font.SysFont(None, 80)
        texto = fuente.render("GEOMETRY DASH", True, AMARILLO)
        pantalla.blit(texto, (ANCHO//2 - texto.get_width()//2, 100))
        
        # Botón Jugar
        boton_jugar = pygame.Rect(300, 250, 200, 60)
        pygame.draw.rect(pantalla, AZUL, boton_jugar)
        fuente = pygame.font.SysFont(None, 50)
        texto = fuente.render("JUGAR", True, (255, 255, 255))
        pantalla.blit(texto, (ANCHO//2 - texto.get_width()//2, 260))
        
        self.botones = [("jugar", boton_jugar)]
    
    def dibujar_menu_niveles(self, pantalla):
        pantalla.fill((20, 20, 60))
        
        # Título
        fuente = pygame.font.SysFont(None, 60)
        texto = fuente.render("SELECCIONA NIVEL", True, AMARILLO)
        pantalla.blit(texto, (ANCHO//2 - texto.get_width()//2, 50))
        
        self.botones = []
        colores = [VERDE, AMARILLO, ROJO]
        
        for i in range(3):
            boton = pygame.Rect(250, 150 + i * 100, 300, 60)
            pygame.draw.rect(pantalla, colores[i], boton)
            fuente = pygame.font.SysFont(None, 50)
            texto = fuente.render(f"NIVEL {i+1}", True, NEGRO)
            pantalla.blit(texto, (ANCHO//2 - texto.get_width()//2, 160 + i * 100))
            self.botones.append((f"nivel_{i+1}", boton))
    
    def verificar_clic(self, posicion):
        for nombre, boton in self.botones:
            if boton.collidepoint(posicion):
                return nombre
        return None

# Función para mostrar mensajes
def mostrar_mensaje(pantalla, texto, color, y, tamaño=60):
    fuente = pygame.font.SysFont(None, tamaño)
    texto_render = fuente.render(texto, True, color)
    x = ANCHO//2 - texto_render.get_width()//2
    pantalla.blit(texto_render, (x, y))
    return texto_render

# Función para esperar tiempo
def esperar_tiempo(segundos):
    tiempo_inicio = time.time()
    while time.time() - tiempo_inicio < segundos:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        reloj.tick(60)

# Crear objetos del juego
juego = Juego()
menu = Menu()

# Bucle principal
ejecutando = True
while ejecutando:
    # Manejar eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
        
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if juego.estado == "menu":
                boton_presionado = menu.verificar_clic(evento.pos)
                if boton_presionado == "jugar":
                    juego.cambiar_estado("seleccion_nivel")
            
            elif juego.estado == "seleccion_nivel":
                boton_presionado = menu.verificar_clic(evento.pos)
                if boton_presionado and boton_presionado.startswith("nivel_"):
                    nivel = int(boton_presionado.split("_")[1])
                    juego.cambiar_nivel(nivel)
                    juego.cambiar_estado("jugando")
            
            # Salto con click izquierdo durante el juego
            elif juego.estado == "jugando" and evento.button == 1:  # Botón izquierdo
                juego.jugador.saltar()
        
        if evento.type == pygame.KEYDOWN:
            if juego.estado == "jugando" and evento.key == pygame.K_SPACE:
                juego.jugador.saltar()
    
    # Actualizar según el estado
    if juego.estado == "menu":
        menu.dibujar_menu_principal(pantalla)
    
    elif juego.estado == "seleccion_nivel":
        menu.dibujar_menu_niveles(pantalla)
    
    elif juego.estado == "jugando":
        nivel_actual = juego.obtener_nivel_actual()
        
        # Actualizar jugador y nivel
        juego.jugador.actualizar(nivel_actual.obstaculos)
        nivel_actual.actualizar()
        
        # Verificar colisiones
        if nivel_actual.verificar_colision(juego.jugador):
            # Game Over
            pantalla.fill(NEGRO)
            mostrar_mensaje(pantalla, "GAME OVER", ROJO, 250)
            mostrar_mensaje(pantalla, "Reiniciando...", (255, 255, 255), 320, 30)
            pygame.display.flip()
            
            esperar_tiempo(1.5)
            juego.reiniciar_nivel()
        
        # Verificar si completó el nivel
        elif nivel_actual.esta_completado():
            # Victoria
            pantalla.fill(NEGRO)
            mostrar_mensaje(pantalla, f"NIVEL {juego.nivel_actual} COMPLETADO!", VERDE, 250)
            mostrar_mensaje(pantalla, "¡GANASTE!", AMARILLO, 320, 40)
            pygame.display.flip()
            
            esperar_tiempo(1.5)
            juego.cambiar_estado("seleccion_nivel")
        
        else:
            # Dibujar juego normal
            nivel_actual.dibujar(pantalla)
            juego.jugador.dibujar(pantalla)
            mostrar_mensaje(pantalla, f"Nivel {juego.nivel_actual}", (255, 255, 255), 20, 30)
    
    # Actualizar pantalla
    pygame.display.flip()
    reloj.tick(60)

pygame.quit()
sys.exit()
