import sys
import pygame
from parametros import (HEIGHT, RUTA_BIRD, WINDOW_SIZE, COLOR_FONDO, FPS, RUTA_CAÑERIA, RUTA_SKYNET
, WIDTH, HEIGHT, ANCHO_SKYNET, ALTURA_SKYNET, G)

from frontend.pajaro import Skynet
pygame.init()

#Se crea la ventana, se le pine nombre y color
window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Flappy_robot")
window.fill(COLOR_FONDO)
pygame.display.update()

#Imagen cañería
pipe = pygame.image.load(RUTA_CAÑERIA)
#Se crea Skynet
Robot = Skynet()

#Se define la función principal
def main():
    run = True
    #Es un loop que corre el juego
    while run:
        clock = pygame.time.Clock()
        pintar_pantalla()
        fisica()

        #Chequea los eventos
        for event in pygame.event.get():
            clock.tick(FPS)

            #Si se apreta la X se acaba el loop del juego
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()


def pintar_pantalla():
    window.fill(COLOR_FONDO)
    window.blit(Robot.imagen, (Robot.x, Robot.y))
    pygame.display.update()

def fisica():
    #gravedad
    Robot.Vy -= G
    Robot.mover()


#Se corre el juego
if __name__ == "__main__":
    main()