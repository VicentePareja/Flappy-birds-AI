import pygame
from parametros import (WIDTH, HEIGHT, RUTA_CAÑERIA, VELOCIDAD_CAÑERIAS
, SPAWN_CAÑERIAS, RUTA_CAÑERIA_INVERSA, ALTO_CAÑERIAS)


class Pipe:
    def __init__(self, altura):
        self.imagen = pygame.image.load(RUTA_CAÑERIA)
        self.x = SPAWN_CAÑERIAS
        self.y = altura
        self.Vx = -VELOCIDAD_CAÑERIAS
        self.Vy = 0
        #self.rect = self.imagen.get_rect()

    def mover(self):
        self.x += self.Vx 
        self.y -= self.Vy


class InvertedPipe:
    def __init__(self, altura):
        self.imagen = pygame.image.load(RUTA_CAÑERIA_INVERSA)
        self.x = SPAWN_CAÑERIAS
        self.y = altura - ALTO_CAÑERIAS
        self.Vx = -VELOCIDAD_CAÑERIAS
        self.Vy = 0
        #self.rect = self.imagen.get_rect()

    def mover(self):
        self.x += self.Vx 
        self.y -= self.Vy