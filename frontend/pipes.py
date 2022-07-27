import pygame
from parametros import WIDTH, HEIGHT, RUTA_CAÑERIA


class Pipe:
    def __init__(self):
        self.imagen = pygame.image.load(RUTA_CAÑERIA)
        self.x = 600
        self.y = 300
        self.Vx = 0
        self.Vy = 0
        #self.rect = self.imagen.get_rect()

    def mover(self):
        self.x += self.Vx 
        self.y -= self.Vy