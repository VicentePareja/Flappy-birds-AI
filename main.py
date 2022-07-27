import sys
import pygame
from parametros import WINDOW_SIZE, COLOR_FONDO, FPS

pygame.init()

#Se crea la ventana, se le pine nombre y color
window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Flappy_robot")
window.fill(COLOR_FONDO)
pygame.display.update()


#Se define la función principal
def main():
    run = True
    #Es un loop que corre el juego
    while run:
        clock = pygame.time.Clock()
        pintar_pantalla()

        #Chequea los eventos
        for event in pygame.event.get():
            clock.tick(FPS)

            #Si se apreta la X se acaba el loop del juego
            if event.type == pygame.QUIT:
                print(event == pygame.QUIT)
                run = False

    pygame.quit()


def pintar_pantalla():
    window.fill(COLOR_FONDO)
    pygame.display.update()





#Se corre el juego
if __name__ == "__main__":
    main()