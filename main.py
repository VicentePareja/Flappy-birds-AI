import sys
import pygame
from parametros import (HEIGHT, RUTA_BIRD, WINDOW_SIZE, COLOR_FONDO, FPS, RUTA_CAÑERIA, RUTA_SKYNET
, WIDTH, HEIGHT, ANCHO_SKYNET, ALTURA_SKYNET)

pygame.init()

#Se crea la ventana, se le pine nombre y color
window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Flappy_robot")
window.fill(COLOR_FONDO)
pygame.display.update()

#Imagen cañería
pipe = pygame.image.load(RUTA_CAÑERIA)
#Imagen pajarito
skynet = pygame.image.load(RUTA_SKYNET)


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
    window.blit(skynet, (WIDTH/2 - int(ANCHO_SKYNET/2), 200))
    pygame.display.update()

def fisica():
    pass

"""class skynet:
    def __init__(self):
        self.imagen = 
        self.x = WIDTH/2 - int(ANCHO_SKYNET/2)
        self.y = 200"""

#Se corre el juego
if __name__ == "__main__":
    main()