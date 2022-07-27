import os

FPS = 60

#Tamaños
WIDTH = 800
HEIGHT = 600
WINDOW_SIZE = WIDTH, HEIGHT
ANCHO_SKYNET = 50
ALTURA_SKYNET = 60
ANCHO_CAÑERIAS = 100
ALTO_CAÑERIAS = 500

#posiciones
SPAWN_CAÑERIAS = 900

#Colores
COLOR_FONDO = (200, 200, 255)

#Rutas
RUTA_CAÑERIA = os.path.join("frontend", "Sprites", "Pipe.png")
RUTA_CAÑERIA_INVERSA = os.path.join("frontend", "Sprites", "Inverted Pipe.png")
RUTA_BIRD = os.path.join("frontend", "Sprites", "Pajaro.png")
RUTA_ROJO = os.path.join("frontend", "Sprites", "Cuadrado Rojo.png")
RUTA_SKYNET = os.path.join("frontend", "Sprites", "SKYNET.png")

#Constantes

G = 0.001
VELOCIDAD_CAÑERIAS = 0.1
DISTANCIA_HORIZONTAL_CAÑERIAS = 2500
DISTANCIA_VERTICAL_CAÑERIAS = 200