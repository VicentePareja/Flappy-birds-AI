import pygame
from parametros import RUTA_SKYNET, WIDTH, ANCHO_SKYNET, HEIGHT

class Skynet(pygame.sprite.Sprite):
    def __init__(self):
        self.imagen = pygame.image.load(RUTA_SKYNET)
        self.x = WIDTH/2 - int(ANCHO_SKYNET/2)
        self.y = 200
        self.Vx = 0
        self.Vy = 0
        self.rect = self.imagen.get_rect()
        self.rect.move_ip(self.x, self.y)
    
    def actualizar_rect(self):
        self.rect = self.rect.move(self.x, self.y)

    def mover(self):
        self.x += self.Vx 
        self.y -= self.Vy
        self.actualizar_rect()
