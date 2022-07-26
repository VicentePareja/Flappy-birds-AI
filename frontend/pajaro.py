import pygame
from parametros import RUTA_SKYNET, WIDTH, ANCHO_SKYNET

class Skynet:
    def __init__(self):
        self.imagen = pygame.image.load(RUTA_SKYNET)
        self.x = WIDTH/2 - int(ANCHO_SKYNET/2)
        self.y = 200
        self.Vx = 0
        self.Vy = 0
        #self.rect = self.imagen.get_rect()

    def mover(self):
        self.x += self.Vx 
        self.y -= self.Vy