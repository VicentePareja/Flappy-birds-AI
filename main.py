import sys
import pygame

pygame.init()

SIZE = 800, 600
window = pygame.display.set_mode(SIZE)



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

main()