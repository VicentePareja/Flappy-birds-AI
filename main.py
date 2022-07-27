import sys
import pygame

pygame.init()

SIZE = 800, 600
window = pygame.display.set_mode(SIZE)

run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print(event == pygame.QUIT)
            run = False

pygame.quit()