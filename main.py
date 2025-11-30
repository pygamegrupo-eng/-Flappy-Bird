import sys
import pygame

# Inicialización de pygame
pygame.init()
ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Geometry Dash Básico")
reloj = pygame.time.Clock()

# Colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
AMARILLO = (255, 255, 0)
AZUL = (100, 100, 255)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
MORADO = (200, 100, 200)

# Constantes del juego
SUELO_Y = ALTO - 50
FPS = 60

# ====================================================================
# MATRICES DE NIVELES (con más espacio inicial)
# ====================================================================

NIVEL_1 = [
    ["pincho", 700],
    ["pincho", 1000],
    ["pincho", 1300],
    ["pincho", 1600],
    ["pincho", 1900],
    ["pincho", 2200],
]

NIVEL_2 = [
    ["pincho", 600],
    ["bloque", 900, SUELO_Y - 25, 120, 25],
    ["pincho", 1200],
    ["bloque", 1500, SUELO_Y - 40, 80, 40],
    ["bloque", 1620, SUELO_Y - 60, 80, 60],
    ["pincho", 2050],
    ["pincho", 2350],
    ["bloque", 2700, SUELO_Y - 30, 180, 30],
    ["pincho", 3000],
    ["bloque", 3300, SUELO_Y - 60, 80, 60],
    ["bloque", 3440, SUELO_Y - 40, 80, 40],
    ["bloque", 3600, SUELO_Y - 30, 100, 30],
    ["bloque", 3800, SUELO_Y - 25, 120, 25],
    ["pincho", 4100]
]

NIVEL_3 = [
    ["pincho", 500],
    ["bloque", 800, SUELO_Y - 25, 120, 25],
    ["pincho", 1000],
    ["bloque", 1300, SUELO_Y - 70, 80, 25],
    ["bloque", 1420, SUELO_Y - 80, 80, 25],
    ["bloque", 1540, SUELO_Y - 90, 80, 25],
    ["pincho", 1700],
    ["pincho", 1850],
]

NIVEL_4 = [
    ["pincho", 650],
    ["pincho", 1000],
    ["bloque", 1300, SUELO_Y - 30, 130, 30],
    ["bloque", 1500, SUELO_Y - 60, 130, 60],
    ["bloque", 1700, SUELO_Y - 90, 130, 90],
    ["pincho", 1900],
    ["pincho", 2100],
    ["bloque", 2350, SUELO_Y - 70, 180, 20],
    ["minipincho", 2580],
    ["minipincho", 2610],
    ["pincho", 2800],
    ["pincho", 3000],
    ["pincho", 3200],
    ["pincho", 3400],
    ["bloque", 3700, SUELO_Y - 25, 400, 25],
    ["bloque", 3700, SUELO_Y - 170, 400, 25],
    ["pincho", 4200],
    ["bloque", 4450, SUELO_Y - 50, 200, 50],
    ["pincho", 4700],
    ["bloque", 4950, SUELO_Y - 40, 160, 40],
    ["minipincho", 5150],
]

NIVEL_5 = [
    # Inicio con mucho espacio para prepararse
    ["pincho", 800],
    ["pincho", 1100],
    ["pincho", 1400],
    
    # Primera escalera más espaciada
    ["bloque", 1700, SUELO_Y - 35, 120, 35],
    ["bloque", 1900, SUELO_Y - 70, 120, 70],
    ["bloque", 2100, SUELO_Y - 105, 120, 105],
    
    # Espacio para respirar
    ["pincho", 2400],
    
    # Plataformas flotantes más espaciadas
    ["bloque", 2700, SUELO_Y - 120, 90, 20],
    ["bloque", 2900, SUELO_Y - 130, 90, 20],
    ["bloque", 3100, SUELO_Y - 140, 90, 20],
    
    # Bajada suave
    ["pincho", 3400],
    ["pincho", 3650],
    
    # Túnel más largo y menos pinchos
    ["bloque", 3950, SUELO_Y - 30, 500, 30],
    ["bloque", 3950, SUELO_Y - 200, 500, 30],
    
    # Menos pinchos en el túnel, más espaciados
    ["minipincho", 4050, SUELO_Y - 60],
    ["minipincho", 4150, SUELO_Y - 60],
    ["minipincho", 4250, SUELO_Y - 60],
    ["minipincho", 4350, SUELO_Y - 60],
    
    # Salida del túnel
    ["pincho", 4600],
    ["pincho", 4850],
    
    # Bloques zigzag más espaciados
    ["bloque", 5100, SUELO_Y - 40, 120, 40],
    ["bloque", 5300, SUELO_Y - 80, 120, 80],
    ["bloque", 5500, SUELO_Y - 120, 120, 120],
    ["bloque", 5700, SUELO_Y - 80, 120, 80],
    ["bloque", 5900, SUELO_Y - 40, 120, 40],
    
    # Sección final más espaciada
    ["pincho", 6150],
    ["pincho", 6400],
    ["pincho", 6650],
    
    # Plataformas finales
    ["bloque", 6900, SUELO_Y - 150, 100, 25],
    ["bloque", 7100, SUELO_Y - 160, 100, 25],
    ["bloque", 7300, SUELO_Y - 170, 100, 25],
    
    # Últimos obstáculos
    ["pincho", 7550],
    ["pincho", 7800],
    
    # Plataforma final de victoria
    ["bloque", 8100, SUELO_Y - 35, 400, 35],
    
    # Final
    ["pincho", 8600],
]

# ====================================================================
# CLASES DEL JUEGO
# ====================================================================

class Jugador:
    def __init__(self, nivel_actual=1):
        self.tamaño = 40
        self.x = 100
        self.y = SUELO_Y - self.tamaño
        self.velocidad_y = 0
        self.gravedad = 0.9
        self.fuerza_salto = -12
        self.fuerza_doble_salto = -10
        self.en_suelo = True
        self.rotacion = 0
        self.puede_doble_salto = False
        self.nivel_actual = nivel_actual
    
    def saltar(self):
        # Primer salto desde el suelo
        if self.en_suelo:
            self.velocidad_y = self.fuerza_salto
            self.en_suelo = False
            # Habilitar doble salto solo desde nivel 3
            if self.nivel_actual >= 3:
                self.puede_doble_salto = True
        # Doble salto en el aire (solo nivel 3 en adelante)
        elif self.puede_doble_salto and self.nivel_actual >= 3:
            self.velocidad_y = self.fuerza_doble_salto
            self.puede_doble_salto = False
    
    def actualizar(self, obstaculos=None):
        # Aplicar física
        self.velocidad_y += self.gravedad
        self.y += self.velocidad_y
        
        # Rotación del cubo mientras está en el aire
        if not self.en_suelo:
            self.rotacion += 8
        else:
            self.rotacion = 0
        
        self.en_suelo = False
        
        # Colisión con el suelo
        if self.y >= SUELO_Y - self.tamaño:
            self.y = SUELO_Y - self.tamaño
            self.velocidad_y = 0
            self.en_suelo = True
            # Restaurar doble salto al tocar el suelo
            if self.nivel_actual >= 3:
                self.puede_doble_salto = False
        
        # Colisión con bloques (solo desde arriba)
        if obstaculos:
            for obstaculo in obstaculos:
                if isinstance(obstaculo, Bloque):
                    rect_jugador = self.obtener_rectangulo()
                    rect_obstaculo = obstaculo.obtener_rectangulo()
                    
                    if (self.velocidad_y >= 0 and 
                        rect_jugador.bottom >= rect_obstaculo.top and
                        rect_jugador.bottom - self.velocidad_y <= rect_obstaculo.top + 10 and
                        rect_jugador.right > rect_obstaculo.left + 5 and
                        rect_jugador.left < rect_obstaculo.right - 5):
                        
                        self.y = rect_obstaculo.top - self.tamaño
                        self.velocidad_y = 0
                        self.en_suelo = True
                        # Restaurar doble salto al tocar bloque
                        if self.nivel_actual >= 3:
                            self.puede_doble_salto = False
    
    def dibujar(self, pantalla):
        # Crear superficie para rotación
        superficie = pygame.Surface((self.tamaño, self.tamaño), pygame.SRCALPHA)
        pygame.draw.rect(superficie, AMARILLO, (0, 0, self.tamaño, self.tamaño))
        
        # Dibujar borde negro
        pygame.draw.rect(superficie, NEGRO, (0, 0, self.tamaño, self.tamaño), 3)
        
        # Rotar superficie
        superficie_rotada = pygame.transform.rotate(superficie, self.rotacion)
        rect_rotado = superficie_rotada.get_rect(center=(self.x + self.tamaño//2, self.y + self.tamaño//2))
        
        pantalla.blit(superficie_rotada, rect_rotado.topleft)
    
    def obtener_rectangulo(self):
        return pygame.Rect(self.x, self.y, self.tamaño, self.tamaño)

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
        pass
    
    def obtener_rectangulo(self):
        return pygame.Rect(self.x, self.y, self.ancho, self.alto)
    
    def esta_fuera(self):
        return self.x + self.ancho < 0

class Pincho(Obstaculo):
    def __init__(self, x, ancho=30, alto=40):
        y = SUELO_Y - alto
        super().__init__(x, y, ancho, alto)
        self.color = MORADO
    
    def dibujar(self, pantalla):
        p1 = (self.x, self.y + self.alto)
        p2 = (self.x + self.ancho, self.y + self.alto)
        p3 = (self.x + self.ancho / 2, self.y)
        pygame.draw.polygon(pantalla, self.color, [p1, p2, p3])
        pygame.draw.polygon(pantalla, NEGRO, [p1, p2, p3], 2)

class MiniPincho(Obstaculo):
    def __init__(self, x, y=None, ancho=18, alto=26):
        if y is None:
            y = SUELO_Y - alto
        super().__init__(x, y, ancho, alto)
        self.color = (255, 230, 100)
    
    def dibujar(self, pantalla):
        p1 = (self.x, self.y + self.alto)
        p2 = (self.x + self.ancho, self.y + self.alto)
        p3 = (self.x + self.ancho / 2, self.y)
        pygame.draw.polygon(pantalla, self.color, [p1, p2, p3])
        pygame.draw.polygon(pantalla, NEGRO, [p1, p2, p3], 2)

class Bloque(Obstaculo):
    def __init__(self, x, y, ancho, alto):
        super().__init__(x, y, ancho, alto)
        self.color = (0, 100, 255)

    def dibujar(self, pantalla):
        pygame.draw.rect(pantalla, self.color, (self.x, self.y, self.ancho, self.alto))
        pygame.draw.rect(pantalla, NEGRO, (self.x, self.y, self.ancho, self.alto), 2)

class Nivel:
    def __init__(self, numero, color_fondo, velocidad=6):
        self.numero = numero
        self.color_fondo = color_fondo
        self.velocidad = velocidad
        self.obstaculos = []
        self.cargar_desde_matriz()
    
    def cargar_desde_matriz(self):
        niveles_data = {
            1: NIVEL_1,
            2: NIVEL_2,
            3: NIVEL_3,
            4: NIVEL_4,
            5: NIVEL_5
        }

        datos = niveles_data.get(self.numero, [])

        for item in datos:
            tipo = item[0]

            if tipo == "pincho":
                x = item[1]
                self.obstaculos.append(Pincho(x))
            
            elif tipo == "minipincho":
                x = item[1]
                if len(item) > 2:
                    y = item[2]
                    self.obstaculos.append(MiniPincho(x, y))
                else:
                    self.obstaculos.append(MiniPincho(x))

            elif tipo == "bloque":
                if len(item) >= 5:
                    x, y, ancho, alto = item[1], item[2], item[3], item[4]
                    self.obstaculos.append(Bloque(x, y, ancho, alto))

    def actualizar(self):
        for obstaculo in self.obstaculos[:]:
            obstaculo.velocidad = self.velocidad
            obstaculo.actualizar()
            if obstaculo.esta_fuera():
                self.obstaculos.remove(obstaculo)
    
    def dibujar(self, pantalla):
        pantalla.fill(self.color_fondo)
        pygame.draw.rect(pantalla, AZUL, (0, SUELO_Y, ANCHO, 50))
        pygame.draw.line(pantalla, NEGRO, (0, SUELO_Y), (ANCHO, SUELO_Y), 3)
        
        # Dibujar primero los bloques (fondo)
        for obstaculo in self.obstaculos:
            if isinstance(obstaculo, Bloque):
                obstaculo.dibujar(pantalla)
        
        # Luego dibujar los pinchos (primer plano)
        for obstaculo in self.obstaculos:
            if not isinstance(obstaculo, Bloque):
                obstaculo.dibujar(pantalla)
    
    def verificar_colision(self, jugador):
        rect_jugador = jugador.obtener_rectangulo()
        for obstaculo in self.obstaculos:
            if rect_jugador.colliderect(obstaculo.obtener_rectangulo()):
                if isinstance(obstaculo, Bloque):
                    # Permitir estar encima del bloque
                    if (jugador.velocidad_y >= 0 and 
                        rect_jugador.bottom >= obstaculo.y and
                        rect_jugador.bottom - jugador.velocidad_y <= obstaculo.y + 10):
                        continue
                return True
        return False
    
    def esta_completado(self):
        return len(self.obstaculos) == 0

class Juego:
    def __init__(self):
        self.estado = "menu"
        self.nivel_actual = 1
        self.jugador = Jugador(self.nivel_actual)
        self.niveles = {
            1: Nivel(1, (50, 50, 150), 6),
            2: Nivel(2, (150, 50, 50), 7),
            3: Nivel(3, (50, 150, 50), 8),
            4: Nivel(4, (120, 50, 150), 7),
            5: Nivel(5, (180, 50, 50), 8)
        }
        self.temporizador_mensaje = 0
        self.mostrando_mensaje = False
        self.tipo_mensaje = ""
    
    def cambiar_estado(self, nuevo_estado):
        self.estado = nuevo_estado
    
    def cambiar_nivel(self, numero_nivel):
        if numero_nivel in self.niveles:
            self.nivel_actual = numero_nivel
            self.jugador = Jugador(self.nivel_actual)
    
    def obtener_nivel_actual(self):
        return self.niveles.get(self.nivel_actual)
    
    def reiniciar_nivel(self):
        nivel = self.nivel_actual
        color = self.niveles[nivel].color_fondo
        vel = self.niveles[nivel].velocidad
        self.niveles[nivel] = Nivel(nivel, color, vel)
        self.jugador = Jugador(self.nivel_actual)
    
    def iniciar_mensaje(self, tipo, duracion_frames):
        self.mostrando_mensaje = True
        self.tipo_mensaje = tipo
        self.temporizador_mensaje = duracion_frames
    
    def actualizar_mensaje(self):
        if self.mostrando_mensaje:
            self.temporizador_mensaje -= 1
            if self.temporizador_mensaje <= 0:
                self.mostrando_mensaje = False
                if self.tipo_mensaje == "game_over":
                    self.reiniciar_nivel()
                elif self.tipo_mensaje == "victoria":
                    self.cambiar_estado("seleccion_nivel")

class Menu:
    def __init__(self):
        self.botones = []
    
    def dibujar_menu_principal(self, pantalla):
        pantalla.fill(NEGRO)
        
        fuente_titulo = pygame.font.SysFont(None, 80)
        texto_titulo = fuente_titulo.render("GEOMETRY DASH", True, AMARILLO)
        pantalla.blit(texto_titulo, (ANCHO//2 - texto_titulo.get_width()//2, 100))
        
        fuente_subtitulo = pygame.font.SysFont(None, 30)
        texto_sub = fuente_subtitulo.render("Versión Mejorada", True, BLANCO)
        pantalla.blit(texto_sub, (ANCHO//2 - texto_sub.get_width()//2, 180))
        
        boton_jugar = pygame.Rect(ANCHO//2 - 100, 300, 200, 60)
        pygame.draw.rect(pantalla, AZUL, boton_jugar)
        pygame.draw.rect(pantalla, BLANCO, boton_jugar, 3)
        
        fuente_boton = pygame.font.SysFont(None, 50)
        texto_boton = fuente_boton.render("JUGAR", True, BLANCO)
        pantalla.blit(texto_boton, (ANCHO//2 - texto_boton.get_width()//2, 310))
        
        fuente_instrucciones = pygame.font.SysFont(None, 25)
        instrucciones = [
            "Controles:",
            "ESPACIO o CLICK para saltar",
            "DOBLE SALTO desde Nivel 3",
            "¡Evita los pinchos!"
        ]
        for i, linea in enumerate(instrucciones):
            texto = fuente_instrucciones.render(linea, True, VERDE)
            pantalla.blit(texto, (ANCHO//2 - texto.get_width()//2, 420 + i * 30))
        
        self.botones = [("jugar", boton_jugar)]
    
    def dibujar_menu_niveles(self, pantalla):
        pantalla.fill((20, 20, 60))
        
        fuente = pygame.font.SysFont(None, 60)
        texto = fuente.render("SELECCIONA NIVEL", True, AMARILLO)
        pantalla.blit(texto, (ANCHO//2 - texto.get_width()//2, 50))
        
        self.botones = []
        colores = [VERDE, AMARILLO, ROJO, MORADO, (255, 100, 0)]
        
        for i in range(5):
            boton = pygame.Rect(ANCHO//2 - 150, 150 + i * 80, 300, 60)
            pygame.draw.rect(pantalla, colores[i], boton)
            pygame.draw.rect(pantalla, NEGRO, boton, 3)
            
            fuente_boton = pygame.font.SysFont(None, 50)
            nivel_texto = f"NIVEL {i+1}"
            
            texto_boton = fuente_boton.render(nivel_texto, True, NEGRO)
            pantalla.blit(texto_boton, (ANCHO//2 - texto_boton.get_width()//2, 165 + i * 80))
            self.botones.append((f"nivel_{i+1}", boton))
    
    def verificar_clic(self, posicion):
        for nombre, boton in self.botones:
            if boton.collidepoint(posicion):
                return nombre
        return None

def mostrar_mensaje(pantalla, texto, color, y, tamaño=60):
    fuente = pygame.font.SysFont(None, tamaño)
    texto_render = fuente.render(texto, True, color)
    x = ANCHO//2 - texto_render.get_width()//2
    pantalla.blit(texto_render, (x, y))

# ====================================================================
# BUCLE PRINCIPAL DEL JUEGO
# ====================================================================

juego = Juego()
menu = Menu()
ejecutando = True

while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
        
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if juego.estado == "menu":
                boton = menu.verificar_clic(evento.pos)
                if boton == "jugar":
                    juego.cambiar_estado("seleccion_nivel")
            
            elif juego.estado == "seleccion_nivel":
                boton = menu.verificar_clic(evento.pos)
                if boton and boton.startswith("nivel_"):
                    nivel = int(boton.split("_")[1])
                    juego.cambiar_nivel(nivel)
                    juego.cambiar_estado("jugando")
            
            elif juego.estado == "jugando" and evento.button == 1:
                if not juego.mostrando_mensaje:
                    juego.jugador.saltar()
        
        if evento.type == pygame.KEYDOWN:
            if juego.estado == "jugando" and evento.key == pygame.K_SPACE:
                if not juego.mostrando_mensaje:
                    juego.jugador.saltar()
            
            # ESC para volver al menú
            if evento.key == pygame.K_ESCAPE:
                if juego.estado == "jugando":
                    juego.cambiar_estado("seleccion_nivel")
                elif juego.estado == "seleccion_nivel":
                    juego.cambiar_estado("menu")
    
    # Renderizado según el estado
    if juego.estado == "menu":
        menu.dibujar_menu_principal(pantalla)
    
    elif juego.estado == "seleccion_nivel":
        menu.dibujar_menu_niveles(pantalla)
    
    elif juego.estado == "jugando":
        nivel_actual = juego.obtener_nivel_actual()
        
        if not juego.mostrando_mensaje:
            # Actualizar lógica del juego
            juego.jugador.actualizar(nivel_actual.obstaculos)
            nivel_actual.actualizar()
            
            # Verificar colisiones
            if nivel_actual.verificar_colision(juego.jugador):
                juego.iniciar_mensaje("game_over", 90)
            
            # Verificar si se completó el nivel
            elif nivel_actual.esta_completado():
                juego.iniciar_mensaje("victoria", 90)
        
        else:
            # Actualizar temporizador de mensaje
            juego.actualizar_mensaje()
        
        # Dibujar todo
        nivel_actual.dibujar(pantalla)
        juego.jugador.dibujar(pantalla)
        
        # Mostrar número de nivel
        mostrar_mensaje(pantalla, f"Nivel {juego.nivel_actual}", BLANCO, 20, 30)
        
        # Mostrar indicador de doble salto para niveles 3+
        if juego.nivel_actual >= 3:
            if juego.jugador.puede_doble_salto:
                mostrar_mensaje(pantalla, "DOBLE SALTO LISTO", VERDE, 50, 25)
            elif not juego.jugador.en_suelo:
                mostrar_mensaje(pantalla, "Doble salto usado", (150, 150, 150), 50, 25)
        
        # Mostrar mensajes
        if juego.mostrando_mensaje:
            # Fondo semi-transparente
            overlay = pygame.Surface((ANCHO, ALTO))
            overlay.set_alpha(180)
            overlay.fill(NEGRO)
            pantalla.blit(overlay, (0, 0))
            
            if juego.tipo_mensaje == "game_over":
                mostrar_mensaje(pantalla, "GAME OVER", ROJO, 250)
                mostrar_mensaje(pantalla, "Reiniciando...", BLANCO, 320, 30)
            elif juego.tipo_mensaje == "victoria":
                mostrar_mensaje(pantalla, f"NIVEL {juego.nivel_actual} COMPLETADO!", VERDE, 220)
                mostrar_mensaje(pantalla, "¡GANASTE!", AMARILLO, 300, 50)
    
    pygame.display.flip()
    reloj.tick(FPS)

pygame.quit()
sys.exit()
