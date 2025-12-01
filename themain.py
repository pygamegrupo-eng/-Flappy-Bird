
import sys
import time
import pygame

# Inicialización de pygame
pygame.init()
pygame.mixer.init() 
ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Geometry Dash Básico - Con Nave")
reloj = pygame.time.Clock()

try:
    pygame.mixer.music.load("sound.mp3")
    pygame.mixer.music.set_volume(0.5)  # Volumen al 50%
except:
    print("No se pudo cargar sound.mp3")

# Colores
NEGRO = (0, 0, 0)
AMARILLO = (255, 255, 0)
AZUL = (100, 100, 255)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
MORADO = (200, 100, 200)

# Constantes del juego
SUELO_Y = ALTO - 50  # Posición Y del suelo
FPS = 60

# ====================================================================
# MATRICES DE NIVELES
# FORMATO CORRECTO:
# ["bloque", x, y, ancho, alto]
# ["pincho", x]
# ["minipincho", x]
# ["portal_nave", x]
# ====================================================================

NIVEL_1 = [
    ["pincho", 500],
    ["pincho", 800],
    ["pincho", 1100],
    ["pincho", 1400],
    ["pincho", 1700],
    ["pincho", 2000],
]

NIVEL_2 = [
    ["pincho", 400],
    ["bloque", 700, SUELO_Y - 25, 120, 25],
    ["pincho", 1000],
    ["bloque", 1300, SUELO_Y - 40, 80, 40],
    ["bloque", 1420, SUELO_Y - 60, 80, 60],
    ["pincho", 1850], ["pincho", 2150],
    ["bloque", 2500, SUELO_Y - 30, 180, 30],
    ["pincho", 2800],
    ["bloque", 3100, SUELO_Y - 60, 80, 60],
    ["bloque", 3240, SUELO_Y - 40, 80, 40],
    ["bloque", 3400, SUELO_Y - 30, 100, 30],
    ["bloque", 3600, SUELO_Y - 25, 120, 25],
    ["pincho", 3900]
]

NIVEL_3 = [
    ["pincho", 400], ["minipincho", 440],
    ["bloque", 700, SUELO_Y - 40, 120, 40],
    ["bloque", 950, SUELO_Y - 70, 80, 25],
    ["bloque", 1200, SUELO_Y - 80, 80, 25],
    ["bloque", 1450, SUELO_Y - 90, 80, 25],
    ["bloque", 1700, SUELO_Y - 100, 80, 25],
    ["bloque", 1950, SUELO_Y - 110, 80, 25],
    ["bloque", 2200, SUELO_Y - 120, 80, 25],
    ["bloque", 2450, SUELO_Y - 130, 80, 25],
] + [["minipincho", x] for x in range(920, 2601, 30)] + [
    ["bloque", 3040, SUELO_Y - 25, 100, 25],
    ["bloque", 3200, SUELO_Y - 50, 90, 75],
    ["pincho", 2800], ["pincho", 3160],
]

NIVEL_4 = [
    ["pincho", 450], ["pincho", 800],
    ["bloque", 1100, SUELO_Y - 30, 130, 30],
    ["bloque", 1300, SUELO_Y - 60, 130, 60],
    ["bloque", 1500, SUELO_Y - 90, 130, 90],
    ["pincho", 1250], ["pincho", 1450],
    ["minipincho", 1650], ["minipincho", 1680],
    ["minipincho", 1900], ["minipincho", 1930], ["minipincho", 1960], ["minipincho", 1990],
    ["minipincho", 2020], ["minipincho", 2050], ["minipincho", 2080], ["minipincho", 2110],
    ["bloque", 1920, SUELO_Y - 70, 180, 20],
    ["pincho", 2400], ["pincho", 2600], ["pincho", 2800], ["pincho", 3000], ["pincho", 3200],
    ["bloque", 3500, SUELO_Y - 25, 400, 25],
    ["bloque", 3500, SUELO_Y - 170, 400, 25],
    ["minipincho", 3620, SUELO_Y - 51], ["minipincho", 3650, SUELO_Y - 51],
    ["minipincho", 3800, SUELO_Y - 51], ["minipincho", 3830, SUELO_Y - 51],
    ["bloque", 3850, SUELO_Y - 50, 200, 50],
    ["pincho", 4250],
    ["bloque", 4300, SUELO_Y - 50, 120, 50],
    ["minipincho", 4370, SUELO_Y - 79], ["minipincho", 4400, SUELO_Y - 79],
    ["pincho", 4650], ["minipincho", 4930], ["bloque", 4950, SUELO_Y - 40, 160, 40], ["minipincho", 5110],
]

NIVEL_5 = [
    ["pincho", 800], ["pincho", 1100], ["pincho", 1400],
    ["bloque", 1700, SUELO_Y - 35, 120, 35],
    ["bloque", 1900, SUELO_Y - 70, 120, 70],
    ["bloque", 2100, SUELO_Y - 105, 120, 105],
    ["pincho", 2360],
    ["bloque", 2400, SUELO_Y - 120, 90, 20],
    ["bloque", 2560, SUELO_Y - 130, 90, 20],
    ["bloque", 2790, SUELO_Y - 140, 90, 20],
    ["pincho", 3400], ["pincho", 3650],
    ["bloque", 3950, SUELO_Y - 30, 500, 30],
    ["bloque", 3950, SUELO_Y - 200, 500, 30],
    ["minipincho", 4090, SUELO_Y - 60],
    ["minipincho", 4300, SUELO_Y - 60],
    ["minipincho", 4500], ["minipincho", 4850],
    ["bloque", 5100, SUELO_Y - 40, 120, 40],
    ["bloque", 5300, SUELO_Y - 80, 120, 80],
    ["bloque", 5500, SUELO_Y - 120, 120, 120],
    ["bloque", 5700, SUELO_Y - 80, 120, 80],
    ["bloque", 5920, SUELO_Y - 40, 120, 40],
    ["pincho", 6150], ["pincho", 6400], ["pincho", 6650],
    ["bloque", 6900, SUELO_Y - 150, 10, 25],
    ["bloque", 7100, SUELO_Y - 160, 30, 25],
    ["bloque", 7300, SUELO_Y - 170, 50, 25],
    ["pincho", 7550], ["pincho", 7800],
    ["bloque", 8100, SUELO_Y - 35, 400, 35],
    ["pincho", 8600]
]

# NIVEL 6 (final) - contiene portal que transforma en nave
NIVEL_6 = [
    ["pincho", 400],
    ["pincho", 440],

    ["bloque", 850, SUELO_Y - 40, 200, 40],
    ["bloque", 1150, SUELO_Y - 100, 150, 20],
    ["bloque", 1400, SUELO_Y - 150, 150, 20],
    ["bloque", 1650, SUELO_Y - 200, 150, 20],
    ["bloque", 2000, SUELO_Y - 250, 40, 20],
    ["minipincho", 2000, SUELO_Y - 276 ],
    ["bloque", 1950, SUELO_Y - 100, 400, 100],
    ["portal_nave", 2400, SUELO_Y - 220],

    ["bloque", 2150, 0, 200, 300],

    ["bloque", 3000, SUELO_Y - 100, 60, 100],
    ["bloque", 3120, SUELO_Y - 140, 60, 140],
    ["bloque", 3250, SUELO_Y - 190, 60, 190],

    ["bloque", 3550, 0, 60, 100],
    ["bloque", 3650, 0, 60, 140],
    ["bloque", 3760, 0, 60, 150],

    ["bloque", 4060, 0, 60, 200],
    ["bloque", 4150, SUELO_Y - 230, 60, 230],

]
# ====================================================================
# CLASES DEL JUEGO
# ====================================================================

class Jugador:
    def __init__(self):
        self.tamaño = 40
        self.x = 100
        self.y = SUELO_Y - self.tamaño
        self.velocidad_y = 0
        self.gravedad = 0.9
        self.fuerza_salto = -12
        self.en_suelo = True

    def saltar(self):
        if self.en_suelo:
            self.velocidad_y = self.fuerza_salto
            self.en_suelo = False

    def actualizar(self, obstaculos=None):
        self.velocidad_y += self.gravedad
        self.y += self.velocidad_y

        self.en_suelo = False

        if self.y >= SUELO_Y - self.tamaño:
            self.y = SUELO_Y - self.tamaño
            self.velocidad_y = 0
            self.en_suelo = True

        if obstaculos:
            for obstaculo in obstaculos:
                if isinstance(obstaculo, Bloque):
                    rect_jugador = self.obtener_rectangulo()
                    rect_obstaculo = obstaculo.obtener_rectangulo()

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

class Nave:
    def __init__(self, x, y, ancho=50, alto=25):
        self.x = x
        self.y = y
        self.ancho = ancho
        self.alto = alto
        self.vel_y = 0
        self.gravedad = 0.6
        self.fuerza_subida = -1.2   # Fuerza al "click"

    def actualizar(self, presionando_click):
        # Si estás apretando el mouse o espacio, sube; si no, cae
        if presionando_click:
            self.vel_y += self.fuerza_subida
        else:
            self.vel_y += self.gravedad

        # Limitar velocidad
        if self.vel_y > 10:
            self.vel_y = 10
        if self.vel_y < -10:
            self.vel_y = -10

        # Mover
        self.y += self.vel_y

        # Limitar a pantalla (no pasar del techo ni del suelo)
        if self.y < 0:
            self.y = 0
            self.vel_y = 0
        if self.y + self.alto > SUELO_Y:
            self.y = SUELO_Y - self.alto
            self.vel_y = 0

    def dibujar(self, pantalla):
        pygame.draw.rect(pantalla, (255, 100, 100), (self.x, self.y, self.ancho, self.alto))
        pygame.draw.rect(pantalla, NEGRO, (self.x, self.y, self.ancho, self.alto), 3)

    def obtener_rectangulo(self):
        return pygame.Rect(self.x, self.y, self.ancho, self.alto)

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

    #Nuevo esta fuera
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

class PortalNave(Obstaculo):
    def __init__(self, x, y, vel=6):
        # Asegurar que el portal reciba correctamente su altura
        if y is None:
            y = SUELO_Y - 120

        super().__init__(x, y, 60, 120)
        self.velocidad = vel

    def dibujar(self, pantalla):
        pygame.draw.rect(pantalla, (0, 200, 200), (self.x, self.y, self.ancho, self.alto))
        pygame.draw.rect(pantalla, NEGRO, (self.x, self.y, self.ancho, self.alto), 3)

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
            5: NIVEL_5,
            6: NIVEL_6
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
                x = item[1]
                y = item[2]
                ancho = item[3]
                alto = item[4]
                self.obstaculos.append(Bloque(x, y, ancho, alto))

            elif tipo == "portal_nave":
                x = item[1]
                y = item[2] if len(item) > 2 else None
                self.obstaculos.append(PortalNave(x, y))


    def actualizar(self):
        for obstaculo in self.obstaculos[:]:
            obstaculo.velocidad = self.velocidad
            obstaculo.actualizar()
            if obstaculo.esta_fuera():
                self.obstaculos.remove(obstaculo)

    def dibujar(self, pantalla):
        pantalla.fill(self.color_fondo)
        pygame.draw.rect(pantalla, AZUL, (0, SUELO_Y, ANCHO, 50))

        for obstaculo in self.obstaculos:
            obstaculo.dibujar(pantalla)
    def verificar_colision(self, jugador):
        # Si está el godmode activado, no hay colisiones
        try:
            if juego.godmode:
                return False
        except NameError:
            pass

        rect_jugador = jugador.obtener_rectangulo()

        for obs in self.obstaculos:

            if isinstance(obs, PortalNave):
                if rect_jugador.colliderect(obs.obtener_rectangulo()):
                    self.obstaculos.remove(obs)
                    return "portal_nave"
                else:
                    continue



            # --- OTROS OBSTÁCULOS ---
            if rect_jugador.colliderect(obs.obtener_rectangulo()):

                # Bloque: permitir caer encima
                if isinstance(obs, Bloque):
                    vel_y = getattr(jugador, 'velocidad_y', getattr(jugador, 'vel_y', 0))
                    if (vel_y >= 0 and rect_jugador.bottom >= obs.y and
                        rect_jugador.bottom - vel_y <= obs.y):
                        return False  # caí encima
                    return True      # golpe lateral = muerte

                # Pinchos / minipinchos = muerte
                return True

        return False

    def esta_completado(self):
        return len(self.obstaculos) == 0

class Juego:
    def __init__(self):
        self.estado = "menu"
        # Godmode
        self.godmode = False
        self.nivel_actual = 1
        self.pausado = False
        self.jugador = Jugador()
        self.modo_nave = False
        self.niveles = {
            1: Nivel(1, (50, 50, 150), 6),
            2: Nivel(2, (150, 50, 50), 7),
            3: Nivel(3, (50, 150, 50), 8),
            4: Nivel(4, (120, 50, 150), 7),
            5: Nivel(5, (180, 50, 50), 8),
            6: Nivel(6, (40, 40, 80), 7)
        }

    def cambiar_estado(self, nuevo_estado):
        self.estado = nuevo_estado

    def cambiar_nivel(self, numero_nivel):
        self.nivel_actual = numero_nivel
        self.jugador = Jugador()
        self.modo_nave = False

    def obtener_nivel_actual(self):
        return self.niveles[self.nivel_actual]

    def reiniciar_nivel(self):
        nivel = self.nivel_actual
        color = self.niveles[nivel].color_fondo
        vel = self.niveles[nivel].velocidad
        self.niveles[nivel] = Nivel(nivel, color, vel)
        self.jugador = Jugador()
        self.modo_nave = False
        try:
            pygame.mixer.music.stop()
            pygame.mixer.music.play(-1)
        except:
            pass

class Menu:
    def __init__(self):
        self.botones = []

    def dibujar_menu_principal(self, pantalla):
        pantalla.fill(NEGRO)

        fuente = pygame.font.SysFont(None, 80)
        texto = fuente.render("GEOMETRY DASH", True, AMARILLO)
        pantalla.blit(texto, (ANCHO//2 - texto.get_width()//2, 100))

        boton_jugar = pygame.Rect(300, 250, 200, 60)
        pygame.draw.rect(pantalla, AZUL, boton_jugar)
        fuente = pygame.font.SysFont(None, 50)
        texto = fuente.render("JUGAR", True, (255, 255, 255))
        pantalla.blit(texto, (ANCHO//2 - texto.get_width()//2, 260))

        self.botones = [("jugar", boton_jugar)]

    def dibujar_menu_niveles(self, pantalla):
        pantalla.fill((20, 20, 60))

        fuente = pygame.font.SysFont(None, 60)
        texto = fuente.render("SELECCIONA NIVEL", True, AMARILLO)
        pantalla.blit(texto, (ANCHO//2 - texto.get_width()//2, 50))

        self.botones = []
        colores = [VERDE, AMARILLO, ROJO, MORADO, AZUL, (255, 140, 0)]

        for i in range(6):
            boton = pygame.Rect(250, 150 + i * 80, 300, 60)
            color = colores[i] if i < len(colores) else AZUL
            pygame.draw.rect(pantalla, color, boton)
            fuente = pygame.font.SysFont(None, 50)
            texto = fuente.render(f"NIVEL {i+1}", True, NEGRO)
            pantalla.blit(texto, (ANCHO//2 - texto.get_width()//2, 160 + i * 80))
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
    return texto_render

def esperar_tiempo(segundos):
    tiempo_inicio = time.time()
    while time.time() - tiempo_inicio < segundos:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        reloj.tick(FPS)

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
                    try:
                        pygame.mixer.music.play(-1)  # -1 = loop infinito
                    except:
                        pass

            elif juego.estado == "jugando" and evento.button == 1:
                # solo saltar si el jugador es Jugador (no Nave)
                if not isinstance(juego.jugador, Nave):
                    juego.jugador.saltar()

        if evento.type == pygame.KEYDOWN:
            if juego.estado == "jugando" and evento.key == pygame.K_SPACE:
                if not isinstance(juego.jugador, Nave):
                    juego.jugador.saltar()
            #Godmode Presionar g activar
            if evento.key == pygame.K_g:
                juego.godmode = not juego.godmode
                print("Godmode:", juego.godmode)
            if evento.key == pygame.K_p and juego.estado == "jugando":
                juego.pausado = not juego.pausado
                if juego.pausado:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
    if juego.estado == "menu":
        menu.dibujar_menu_principal(pantalla)

    elif juego.estado == "seleccion_nivel":
        menu.dibujar_menu_niveles(pantalla)

    elif juego.estado == "jugando":
        if juego.pausado:
            # Dibujar sin actualizar
            nivel_actual = juego.obtener_nivel_actual()
            nivel_actual.dibujar(pantalla)
            juego.jugador.dibujar(pantalla)
            mostrar_mensaje(pantalla, f"Nivel {juego.nivel_actual}", (255, 255, 255), 20, 30)
            
            # Pantalla de pausa
            overlay = pygame.Surface((ANCHO, ALTO))
            overlay.set_alpha(150)
            overlay.fill(NEGRO)
            pantalla.blit(overlay, (0, 0))
            mostrar_mensaje(pantalla, "PAUSA", AMARILLO, 250, 80)
            mostrar_mensaje(pantalla, "Presiona P para continuar", (255, 255, 255), 340, 30)
        else:
            nivel_actual = juego.obtener_nivel_actual()

            # actualizar y mover jugador dependiendo si es Nave o Jugador
            if isinstance(juego.jugador, Nave):
                keys = pygame.key.get_pressed()
                presionando = pygame.mouse.get_pressed()[0] or keys[pygame.K_SPACE]
                juego.jugador.actualizar(presionando)
            else:
                juego.jugador.actualizar(nivel_actual.obstaculos)

            nivel_actual.actualizar()

            col = nivel_actual.verificar_colision(juego.jugador)
            if col == True:
                pantalla.fill(NEGRO)
                mostrar_mensaje(pantalla, "GAME OVER", ROJO, 250)
                mostrar_mensaje(pantalla, "Reiniciando...", (255, 255, 255), 320, 30)
                pygame.display.flip()
                esperar_tiempo(1.5)
                juego.reiniciar_nivel()

            elif col == "portal_nave":
                juego.jugador = Nave(juego.jugador.x, juego.jugador.y)
                juego.modo_nave = True

            elif nivel_actual.esta_completado():
                pantalla.fill(NEGRO)
                mostrar_mensaje(pantalla, f"NIVEL {juego.nivel_actual} COMPLETADO!", VERDE, 250)
                mostrar_mensaje(pantalla, "¡GANASTE!", AMARILLO, 320, 40)
                pygame.display.flip()
                pygame.mixer.music.stop()
                esperar_tiempo(1.5)
                juego.cambiar_estado("seleccion_nivel")

            else:
                nivel_actual.dibujar(pantalla)
                juego.jugador.dibujar(pantalla)
                mostrar_mensaje(pantalla, f"Nivel {juego.nivel_actual}", (255, 255, 255), 20, 30)

    pygame.display.flip()
    reloj.tick(FPS)

pygame.quit()
sys.exit()
