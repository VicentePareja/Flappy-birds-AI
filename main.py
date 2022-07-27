import sys
import pygame
from parametros import WINDOW_SIZE

pygame.init()


window = pygame.display.set_mode(WINDOW_SIZE)



def main():
    run = True
    #Es un loop que corre el juego
    while run:
        #Chequea los eventos
        for event in pygame.event.get():

            #Si se apreta la X se acaba el loop del juego
            if event.type == pygame.QUIT:
                print(event == pygame.QUIT)
                run = False

    pygame.quit()




#Se corre el juego
if __name__ == "__main__":
    main()