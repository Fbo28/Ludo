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

#tabero
tm=pygame.display.set_mode((900,600))
pygame.display.set_caption("LudoMania")

while True:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()

        pygame.display.update()

