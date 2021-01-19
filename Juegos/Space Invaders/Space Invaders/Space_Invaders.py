import pygame
from pygame.locals import *
import random

pygame.init()

ancho=800
alto=600
cantidadMarcianos=10

pantalla=pygame.display.set_mode((ancho,alto))
pygame.display.set_caption("Juego Python")#cambian el nombre de la ventana
pygame.key.set_repeat(1,25)
reloj = pygame.time.Clock()

imagenNave = pygame.image.load("imagenes/nave.png")
rectanguloNave = imagenNave.get_rect()

imagenUfo = pygame.image.load("imagenes/ufo.png")
rectanguloUfo=imagenUfo.get_rect()

imagen = pygame.image.load("imagenes/spaceinvader.png")#Marciano
rectangulosMarcianos={}
marcianosVisible={}
velocidadesX={}
velocidadesY={}

imagenDisparo = pygame.image.load("imagenes/disparo.png")
rectanguloDisparo = imagenDisparo.get_rect()

imagenPresent = pygame.image.load("imagenes/invadersIntro.png")
rectanguloPresent = imagenPresent.get_rect()
rectanguloPresent.top=60
rectanguloPresent.left=80

letra30 = pygame.font.SysFont("Arial",30)
imagenTextoPresent = letra30.render('Pulsa Espacio para jugar',True,(200,200,200),(0,0,0))
rectanguloTextoPresent = imagenTextoPresent.get_rect()
rectanguloTextoPresent.centerx=pantalla.get_rect().centerx
rectanguloTextoPresent.centery=520

letra18 = pygame.font.SysFont("Arial",18)

partidaEnMarcha=True

while partidaEnMarcha:

    #---Presentación
    pantalla.fill((0,0,0))
    pantalla.blit(imagenPresent,rectanguloPresent)
    pantalla.blit(imagenTextoPresent,rectanguloTextoPresent)
    pygame.display.flip()

    entrarAlJuego = False
    while not entrarAlJuego:
        pygame.time.wait(100)
        for event in pygame.event.get(KEYUP):
            if event.key == K_SPACE:
                entrarAlJuego=True

    #----Comienzo de una sesion de juego
    puntos=0
    rectanguloNave.left=ancho/2
    rectanguloNave.top=alto-50
    rectanguloUfo.top=20

    for i in range(0,cantidadMarcianos+1):
        rectangulosMarcianos[i]=imagen.get_rect()
        rectangulosMarcianos[i].left=random.randrange(50,751)
        rectangulosMarcianos[i].top=random.randrange(10,301)
        marcianosVisible[i]=True
        velocidadesX[i]=3
        velocidadesY[i]=3

    disparoActivo=False
    ufoVisible=True
    terminado=False

    while not terminado:
        #------Comprobar acciones del usuario
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                terminado=True
                partidaEnMarcha=False

        keys = pygame.key.get_pressed()
        if keys[K_LEFT]:
            rectanguloNave.left-=8
        if keys[K_RIGHT]:
            rectanguloNave.left+=8
        if keys[K_SPACE] and not disparoActivo:
            disparoActivo=True
            rectanguloDisparo.left=rectanguloNave.left+18
            rectanguloDisparo.top=rectanguloNave.top-25
    
        #-----Actualizar estado
        for i in range(0,cantidadMarcianos+1):
            rectangulosMarcianos[i].left+=velocidadesX[i]
            rectangulosMarcianos[i].top+=velocidadesY[i]
            if rectangulosMarcianos[i].left < 0 or rectangulosMarcianos[i].right > ancho:
                velocidadesX[i]=-velocidadesX[i]
            if rectangulosMarcianos[i].top < 0 or rectangulosMarcianos[i].bottom > alto:
                velocidadesY[i] = -velocidadesY[i]

        #---Controlamos que la nave no se salga por el borde de la pantalla
        if rectanguloNave.left < 0:
            rectanguloNave.left=0
        if rectanguloNave.right > ancho:
            rectanguloNave.right=ancho

        rectanguloUfo.left+=2
        if rectanguloUfo.right>ancho:
            rectanguloUfo.left=0

        if disparoActivo:
            rectanguloDisparo.top-=6
            if rectanguloDisparo.top <=0:
                disparoActivo=False

        #---Comprobar Colisiones
        for i in range(0,cantidadMarcianos+1):
            if marcianosVisible[i]:
                if rectanguloNave.colliderect(rectangulosMarcianos[i]):
                    terminado=True

                if disparoActivo:
                    if rectanguloDisparo.colliderect(rectangulosMarcianos[i]):
                        marcianosVisible[i]=False
                        disparoActivo=False
                        puntos+=10

        if disparoActivo:
            if rectanguloDisparo.colliderect(rectanguloUfo):
                ufoVisible=False
                disparoActivo=False
                puntos+=50

        cantidadMarcianosVisibles=0
        for i in range(0,cantidadMarcianos+1):
            if marcianosVisible[i]:
                cantidadMarcianosVisibles=cantidadMarcianosVisibles+1

        if not ufoVisible and cantidadMarcianosVisibles==0:
            terminado=True

        #----Dibujar elementos en pantalla
        pantalla.fill((0,0,0))
        for i in range(0,cantidadMarcianos+1):
            if marcianosVisible[i]:
                pantalla.blit(imagen,rectangulosMarcianos[i])#marcianos
        if ufoVisible:
            pantalla.blit(imagenUfo,rectanguloUfo)
        if disparoActivo:
            pantalla.blit(imagenDisparo,rectanguloDisparo)
        pantalla.blit(imagenNave,rectanguloNave)

        imagenPuntos = letra18.render('Puntos '+str(puntos),True,(200,200,200),(0,0,0))
        rectanguloPuntos=imagenPuntos.get_rect()
        rectanguloPuntos.left=10
        rectanguloPuntos.top=10
        pantalla.blit(imagenPuntos,rectanguloPuntos)
        pygame.display.flip()

        #----Ralentizar hasta 50 fps
        reloj.tick(50)
#----Final de partida
pygame.quit()