import sys
import pygame, random
from parametros import (HEIGHT, RUTA_BIRD, WINDOW_SIZE, COLOR_FONDO, FPS, RUTA_CAÑERIA, RUTA_SKYNET
, WIDTH, HEIGHT, ANCHO_SKYNET, ALTURA_SKYNET, G, DISTANCIA_HORIZONTAL_CAÑERIAS, DISTANCIA_VERTICAL_CAÑERIAS)

from frontend.pajaro import Skynet
from frontend.pipes import Pipe, InvertedPipe

pygame.init()

#Se crea la ventana, se le pine nombre y color
window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Flappy_robot")
window.fill(COLOR_FONDO)
pygame.display.update()

#Cañerías
Pipes = []
#Se crea Skynet
Robot = Skynet()


#Se define la función principal
def main():
    run = True
    frame_actual = 0
    generar_pipes()
    #Es un loop que corre el juego
    while run:
        frame_actual += 1
        clock = pygame.time.Clock()
        pintar_pantalla()
        fisica()
        run = handlekeyboard(clock)


        #Chequea los eventos
        

        if frame_actual % DISTANCIA_HORIZONTAL_CAÑERIAS == 0:
            generar_pipes()

    pygame.quit()


def pintar_pantalla():
    
    window.fill(COLOR_FONDO)
    
    window.blit(Robot.imagen, (Robot.x, Robot.y))
    for pipe in Pipes:
        window.blit(pipe.imagen, (pipe.x, pipe.y))
    pygame.display.update()

suelo = pygame.Rect((0,550), (800, 50))
def fisica():
    #gravedad
    Robot.Vy -= G
    Robot.mover()
    if Robot.rect.colliderect(suelo):
        print("chocaste")

def handlekeyboard(clock):
    for event in pygame.event.get():
            clock.tick(FPS)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    Robot.Vy = 0.3
            if event.type == pygame.QUIT:
                
                return False

    for pipe in Pipes:
        pipe.mover()
    
    return True

def generar_pipes():
    altura = random.randint(100,600)
    Pipes.append(Pipe(altura))
    Pipes.append(InvertedPipe(altura - DISTANCIA_VERTICAL_CAÑERIAS))


#Se corre el juego
if __name__ == "__main__":
    main()