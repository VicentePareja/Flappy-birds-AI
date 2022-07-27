import pygame
from parametros import (HEIGHT, RUTA_BIRD, WINDOW_SIZE, COLOR_FONDO, FPS, RUTA_CAÑERIA, RUTA_SKYNET
, WIDTH, HEIGHT, ANCHO_SKYNET, ALTURA_SKYNET, G)
window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Flappy_robot")
window.fill(COLOR_FONDO)
pygame.display.update()

imagen_1 = pygame.image.load(RUTA_SKYNET)
rect_1 = imagen_1.get_rect()
rect_1.move_ip(400, 200)

imagen_2 = pygame.image.load(RUTA_SKYNET)
rect_2 = imagen_1.get_rect()
rect_2.move_ip(100, 200)

while True:
    window.fill(COLOR_FONDO)
    window.blit(imagen_1, rect_1)
    window.blit(imagen_2, rect_2)
    rect_2.x += 1
    pygame.display.update()