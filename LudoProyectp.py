import pygame,sys
from pygame.locals import *

pygame.init()

#colores
sorpresa = (86,160,25)
blanco = (255,255,255)
negro = (0,0,0)
rojo = (255,0,0)
azul = (0,0,255)
verde = (0,255,0)
amarillo = (255,255,0)
fondo = (255,250,205)

#Triángulos
triazul=[(400,350),(230,470),(230,230)]
trirojo=[(400,350),(570,470),(230,470)]
triverde=[(400,350),(570,470),(570,230)]
triamarillo=[(400,350),(230,230),(570,230)]



#Coordenadas


#tabero
tm=pygame.display.set_mode((900,700))
pygame.display.set_caption("LudoParaPobres")
tm.fill(fondo)



#board
pygame.draw.line(tm,negro,(30,30),(30,670),3)
pygame.draw.line(tm,negro,(30,30),(870,30),3)
pygame.draw.line(tm,negro,(30,670),(870,670),3)
pygame.draw.line(tm,negro,(870,30),(870,670),3)
pygame.draw.line(tm,negro,(770,30),(770,670),3)
pygame.draw.circle(tm,rojo,(130,570),90)
pygame.draw.circle(tm,verde,(670,570),90)
pygame.draw.circle(tm,azul,(130,130),90)
pygame.draw.circle(tm,amarillo,(670,130),90)
pygame.draw.circle(tm,negro,(130,570),93,4)
pygame.draw.circle(tm,negro,(670,570),93,4)
pygame.draw.circle(tm,negro,(130,130),93,4)
pygame.draw.circle(tm,negro,(670,130),93,4)
#Rojo
pygame.draw.circle(tm,blanco,(160,540),20)
pygame.draw.circle(tm,blanco,(160,600),20)
pygame.draw.circle(tm,blanco,(100,540),20)
pygame.draw.circle(tm,blanco,(100,600),20)
pygame.draw.circle(tm,negro,(160,540),20,3)
pygame.draw.circle(tm,negro,(160,600),20,3)
pygame.draw.circle(tm,negro,(100,540),20,3)
pygame.draw.circle(tm,negro,(100,600),20,3)
#Azul
pygame.draw.circle(tm,blanco,(160,100),20)
pygame.draw.circle(tm,blanco,(160,160),20)
pygame.draw.circle(tm,blanco,(100,100),20)
pygame.draw.circle(tm,blanco,(100,160),20)
pygame.draw.circle(tm,negro,(160,100),20,3)
pygame.draw.circle(tm,negro,(160,160),20,3)
pygame.draw.circle(tm,negro,(100,100),20,3)
pygame.draw.circle(tm,negro,(100,160),20,3)
#Amarillo
pygame.draw.circle(tm,blanco,(700,100),20)
pygame.draw.circle(tm,blanco,(700,160),20)
pygame.draw.circle(tm,blanco,(640,100),20)
pygame.draw.circle(tm,blanco,(640,160),20)
pygame.draw.circle(tm,negro,(700,100),20,3)
pygame.draw.circle(tm,negro,(700,160),20,3)
pygame.draw.circle(tm,negro,(640,100),20,3)
pygame.draw.circle(tm,negro,(640,160),20,3)
#Verde
pygame.draw.circle(tm,blanco,(700,540),20)
pygame.draw.circle(tm,blanco,(700,600),20)
pygame.draw.circle(tm,blanco,(640,540),20)
pygame.draw.circle(tm,blanco,(640,600),20)
pygame.draw.circle(tm,negro,(700,540),20,3)
pygame.draw.circle(tm,negro,(700,600),20,3)
pygame.draw.circle(tm,negro,(640,540),20,3)
pygame.draw.circle(tm,negro,(640,600),20,3)

#Pista
pygame.draw.rect(tm,blanco,(40,230,720,240))
pygame.draw.rect(tm,blanco,(230,40,340,620))
pygame.draw.line(tm,negro,(40,470),(40,230),3)
pygame.draw.line(tm,negro,(760,470),(760,230),3)
pygame.draw.line(tm,negro,(40,230),(760,230),3)
pygame.draw.line(tm,negro,(760,470),(40,470),3)
pygame.draw.line(tm,negro,(230,40),(570,40),3)
pygame.draw.line(tm,negro,(230,660),(570,660),3)
pygame.draw.line(tm,negro,(230,40),(230,660),3)
pygame.draw.line(tm,negro,(570,40),(570,660),3)
pygame.draw.polygon(tm,azul,triazul)
pygame.draw.polygon(tm,negro,triazul,3)
pygame.draw.polygon(tm,rojo,trirojo)
pygame.draw.polygon(tm,negro,trirojo,3)
pygame.draw.polygon(tm,amarillo,triamarillo)
pygame.draw.polygon(tm,negro,triamarillo,3)
pygame.draw.polygon(tm,verde,triverde)
pygame.draw.polygon(tm,negro,triverde,3)

#home
#rojo
pygame.draw.circle(tm,blanco,(400,390),20)
pygame.draw.circle(tm,blanco,(400,440),20)
pygame.draw.circle(tm,blanco,(360,415),20)
pygame.draw.circle(tm,blanco,(440,415),20)
pygame.draw.circle(tm,negro,(400,390),20,2)
pygame.draw.circle(tm,negro,(400,440),20,2)
pygame.draw.circle(tm,negro,(360,415),20,2)
pygame.draw.circle(tm,negro,(440,415),20,2)
#amarillo
pygame.draw.circle(tm,blanco,(400,310),20)
pygame.draw.circle(tm,blanco,(400,260),20)
pygame.draw.circle(tm,blanco,(440,285),20)
pygame.draw.circle(tm,blanco,(360,285),20)
pygame.draw.circle(tm,negro,(400,310),20,2)
pygame.draw.circle(tm,negro,(400,260),20,2)
pygame.draw.circle(tm,negro,(440,285),20,2)
pygame.draw.circle(tm,negro,(360,285),20,2)
#verde
pygame.draw.circle(tm,blanco,(480,350),20)
pygame.draw.circle(tm,blanco,(540,350),20)
pygame.draw.circle(tm,blanco,(510,390),20)
pygame.draw.circle(tm,blanco,(510,310),20)
pygame.draw.circle(tm,negro,(480,350),20,2)
pygame.draw.circle(tm,negro,(540,350),20,2)
pygame.draw.circle(tm,negro,(510,390),20,2)
pygame.draw.circle(tm,negro,(510,310),20,2)
#azul
pygame.draw.circle(tm,blanco,(320,350),20)
pygame.draw.circle(tm,blanco,(260,350),20)
pygame.draw.circle(tm,blanco,(290,310),20)
pygame.draw.circle(tm,blanco,(290,390),20)
pygame.draw.circle(tm,negro,(320,350),20,2)
pygame.draw.circle(tm,negro,(260,350),20,2)
pygame.draw.circle(tm,negro,(290,310),20,2)
pygame.draw.circle(tm,negro,(290,390),20,2)

#fichas
#rojo
pygame.draw.circle(tm,rojo,(160,540),10)
pygame.draw.circle(tm,rojo,(160,600),10)
pygame.draw.circle(tm,rojo,(100,540),10)
pygame.draw.circle(tm,rojo,(100,600),10)
pygame.draw.circle(tm,negro,(160,540),10,2)
pygame.draw.circle(tm,negro,(160,600),10,2)
pygame.draw.circle(tm,negro,(100,540),10,2)
pygame.draw.circle(tm,negro,(100,600),10,2)
#azul
pygame.draw.circle(tm,azul,(160,100),10)
pygame.draw.circle(tm,azul,(160,160),10)
pygame.draw.circle(tm,azul,(100,100),10)
pygame.draw.circle(tm,azul,(100,160),10)
pygame.draw.circle(tm,negro,(160,100),10,2)
pygame.draw.circle(tm,negro,(160,160),10,2)
pygame.draw.circle(tm,negro,(100,100),10,2)
pygame.draw.circle(tm,negro,(100,160),10,2)
#amarillo
pygame.draw.circle(tm,amarillo,(700,100),10)
pygame.draw.circle(tm,amarillo,(700,160),10)
pygame.draw.circle(tm,amarillo,(640,100),10)
pygame.draw.circle(tm,amarillo,(640,160),10)
pygame.draw.circle(tm,negro,(700,100),10,2)
pygame.draw.circle(tm,negro,(700,160),10,2)
pygame.draw.circle(tm,negro,(640,100),10,2)
pygame.draw.circle(tm,negro,(640,160),10,2)
#verde
pygame.draw.circle(tm,verde,(700,540),10)
pygame.draw.circle(tm,verde,(700,600),10)
pygame.draw.circle(tm,verde,(640,540),10)
pygame.draw.circle(tm,verde,(640,600),10)
pygame.draw.circle(tm,negro,(700,540),10,2)
pygame.draw.circle(tm,negro,(700,600),10,2)
pygame.draw.circle(tm,negro,(640,540),10,2)
pygame.draw.circle(tm,negro,(640,600),10,2)

#casillas
pygame.draw.line(tm,negro,(343.34,40),(343.34,230),3)
pygame.draw.line(tm,negro,(456.68,40),(456.68,230),3)
pygame.draw.line(tm,negro,(343.34,660),(343.34,470),3)
pygame.draw.line(tm,negro,(456.68,660),(456.68,470),3)
pygame.draw.line(tm,negro,(40,310),(230,310),3)
pygame.draw.line(tm,negro,(40,390),(230,390),3)
pygame.draw.line(tm,negro,(760,310),(570,310),3)
pygame.draw.line(tm,negro,(760,390),(570,390),3)




#400,350
while True:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()

        pygame.display.update()

