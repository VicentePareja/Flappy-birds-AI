# segun yo deberia ser 
# una clase para el pajaro, y clase para tuberias
# quizas una para el jugador que lleve la cuenta de puntajes y ese tipo de cosas
# tambien se puede hacer como diccionario
# clase logica
import pygame

class Personaje(pygame.sprite.Sprite):

     def __init__(self, posicion, velocidad, imagen):
        super().__init__()
        self.posicion = posicion
        self.velocidad = velocidad 
        self.image = pygame.image.load("Player_Sprite_R.png")
        self.rect = self.image.get_rect()
    
class Tuberia(pygame.sprite.Sprite):
    def __init__(self, posicion, altura, ancho, imagen):
        super().__init__()
        self.posicion = posicion
        self.altura = altura
        self.ancho = ancho
        self.image = pygame.image.load("Player_Sprite_R.png")
        self.rect = self.image.get_rect()
    
class Jugador:
    def __init__(self, puntaje, nombre, nivel):
        self.puntaje = puntaje
        self.nombre = nombre
        self.nivel = nivel

class Logica:
    def __init__(self, personaje, jugador):
        self.personaje = personaje
        self.tuberias_pantalla = list()
        self.tuberias_fuera = list()
        self.jugador = jugador
        self.tuberia_colision = None

    def impulsar(self):
        self.personaje.velocidad = p.velocidad_click
    
    def actualizar(self):
        self.aplicar_fisica()
        self.mover_personaje()
        self.mover_tuberias()
        self.chequear_colision()
    
    def aplicar_fisica(self):
        self.personaje.velocidad -= p.desaceleracion

    def mover_personaje(self):
        self.personaje.posicion += self.personaje.velocidad

    def mover_tuberias(self):
        pass
    
    def chequear_colision(self):
        if self.personaje.rect.colliderect(self.tuberia.rect_coffe):





