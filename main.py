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
        handlekeyboard(clock)


        #Chequea los eventos
        

    pygame.quit()


def pintar_pantalla():
    
    window.fill(COLOR_FONDO)
    
    window.blit(Robot.imagen, (Robot.x, Robot.y))
    pygame.display.update()

suelo = pygame.Rect((0,550), (800, 50))
def fisica():
    #gravedad
    Robot.Vy -= G
    Robot.mover()
    if Robot.rect.colliderect(suelo):
        print("chocaste")

def handlekeyboard(clock):
    global run
    for event in pygame.event.get():
            clock.tick(FPS)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    Robot.Vy = 0.3
            if event.type == pygame.QUIT:
                run = False



#Se corre el juego
if __name__ == "__main__":
    main()