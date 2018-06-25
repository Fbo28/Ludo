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
pygame.draw.circle(tm,rojo,(130,570),90,4)
pygame.draw.circle(tm,verde,(670,570),90,4)
pygame.draw.circle(tm,azul,(130,130),90,4)
pygame.draw.circle(tm,amarillo,(670,130),90,4)
pygame.draw.circle(tm,negro,(130,570),93,4)
pygame.draw.circle(tm,negro,(670,570),93,4)
pygame.draw.circle(tm,negro,(130,130),93,4)
pygame.draw.circle(tm,negro,(670,130),93,4)

while True:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()

        pygame.display.update()



