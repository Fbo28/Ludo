import pygame,sys
from pygame.locals import *
import random
def dado():
    return random.randint(1,6)

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
moveazul1={1:(160,100),6:(120,251),7:(145,285),8:(184,287),9:(207,250),10:(252,204),11:(317,180),12:(321,180),13:(250,122),14:(248,76),15:(317,57),16:(367,65),17:(425,71),18:(477,51),19:(545,79),20:(544,124),21:(480,141),22:(476,186),23:(536,206),24:(584,249),25:(611,284),26:(650,282),27:(677,251),28:(711,250),29:(739,284),30:(725,326),31:(726,367),32:(739,408),33:(711,446),34:(676,445),35:(650,408),36:(611,409),37:(587,444),38:(541,489),39:(474,512),40:(475,522),41:(541,576),42:(542,616),43:(478,636),44:(426,626),45:(366,630),46:(309,634),47:(254,616),48:(255,569),49:(318,555),50:(315,510),51:(254,487),52:(209,447),53:(183,408),54:(146,407),55:(120,446),56:(83,448),57:(52,408),58:(66,368),59:(117,349),60:(149,350),61:(178,350),62:(213,354)}
moveazul2={1:(160,160),6:(120,251),7:(145,285),8:(184,287),9:(207,250),10:(252,204),11:(317,180),12:(321,180),13:(250,122),14:(248,76),15:(317,57),16:(367,65),17:(425,71),18:(477,51),19:(545,79),20:(544,124),21:(480,141),22:(476,186),23:(536,206),24:(584,249),25:(611,284),26:(650,282),27:(677,251),28:(711,250),29:(739,284),30:(725,326),31:(726,367),32:(739,408),33:(711,446),34:(676,445),35:(650,408),36:(611,409),37:(587,444),38:(541,489),39:(474,512),40:(475,522),41:(541,576),42:(542,616),43:(478,636),44:(426,626),45:(366,630),46:(309,634),47:(254,616),48:(255,569),49:(318,555),50:(315,510),51:(254,487),52:(209,447),53:(183,408),54:(146,407),55:(120,446),56:(83,448),57:(52,408),58:(66,368),59:(117,349),60:(149,350),61:(178,350),62:(213,354)}
moveazul3={1:(100,100),6:(120,251),7:(145,285),8:(184,287),9:(207,250),10:(252,204),11:(317,180),12:(321,180),13:(250,122),14:(248,76),15:(317,57),16:(367,65),17:(425,71),18:(477,51),19:(545,79),20:(544,124),21:(480,141),22:(476,186),23:(536,206),24:(584,249),25:(611,284),26:(650,282),27:(677,251),28:(711,250),29:(739,284),30:(725,326),31:(726,367),32:(739,408),33:(711,446),34:(676,445),35:(650,408),36:(611,409),37:(587,444),38:(541,489),39:(474,512),40:(475,522),41:(541,576),42:(542,616),43:(478,636),44:(426,626),45:(366,630),46:(309,634),47:(254,616),48:(255,569),49:(318,555),50:(315,510),51:(254,487),52:(209,447),53:(183,408),54:(146,407),55:(120,446),56:(83,448),57:(52,408),58:(66,368),59:(117,349),60:(149,350),61:(178,350),62:(213,354)}
moveazul4={1:(100,160),6:(120,251),7:(145,285),8:(184,287),9:(207,250),10:(252,204),11:(317,180),12:(321,180),13:(250,122),14:(248,76),15:(317,57),16:(367,65),17:(425,71),18:(477,51),19:(545,79),20:(544,124),21:(480,141),22:(476,186),23:(536,206),24:(584,249),25:(611,284),26:(650,282),27:(677,251),28:(711,250),29:(739,284),30:(725,326),31:(726,367),32:(739,408),33:(711,446),34:(676,445),35:(650,408),36:(611,409),37:(587,444),38:(541,489),39:(474,512),40:(475,522),41:(541,576),42:(542,616),43:(478,636),44:(426,626),45:(366,630),46:(309,634),47:(254,616),48:(255,569),49:(318,555),50:(315,510),51:(254,487),52:(209,447),53:(183,408),54:(146,407),55:(120,446),56:(83,448),57:(52,408),58:(66,368),59:(117,349),60:(149,350),61:(178,350),62:(213,354)}
#contadores
conazul1=1
azul1=moveazul1[conazul1]
conzaul2=1
azul2=moveazul2[conzaul2]
conazul3=1
azul3=moveazul3[conazul3]
conazul4=1
azul4=moveazul4[conazul4]




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

#fichas
#Rojo
#1
pygame.draw.circle(tm,blanco,(160,540),20)
pygame.draw.circle(tm,negro,(160,540),20,3)
#2
pygame.draw.circle(tm,blanco,(160,600),20)
pygame.draw.circle(tm,negro,(160,600),20,3)

#3
pygame.draw.circle(tm,blanco,(100,540),20)
pygame.draw.circle(tm,negro,(100,540),20,3)

#4
pygame.draw.circle(tm,blanco,(100,600),20)
pygame.draw.circle(tm,negro,(100,600),20,3)

#Azul
#1
pygame.draw.circle(tm,blanco,(160,100),20)
pygame.draw.circle(tm,negro,(160,100),20,3)
#2
pygame.draw.circle(tm,blanco,(160,160),20)
pygame.draw.circle(tm,negro,(160,160),20,3)
#3
pygame.draw.circle(tm,blanco,(100,100),20)
pygame.draw.circle(tm,negro,(100,100),20,3)
#4
pygame.draw.circle(tm,blanco,(100,160),20)
pygame.draw.circle(tm,negro,(100,160),20,3)

#Amarillo
#1
pygame.draw.circle(tm,blanco,(700,100),20)
pygame.draw.circle(tm,negro,(700,100),20,3)
#2
pygame.draw.circle(tm,blanco,(700,160),20)
pygame.draw.circle(tm,negro,(700,160),20,3)
#3
pygame.draw.circle(tm,blanco,(640,100),20)
pygame.draw.circle(tm,negro,(640,100),20,3)
#4
pygame.draw.circle(tm,blanco,(640,160),20)
pygame.draw.circle(tm,negro,(640,160),20,3)

#Verde
#1
pygame.draw.circle(tm,blanco,(700,540),20)
pygame.draw.circle(tm,negro,(700,540),20,3)
#2
pygame.draw.circle(tm,blanco,(700,600),20)
pygame.draw.circle(tm,negro,(700,600),20,3)
#3
pygame.draw.circle(tm,blanco,(640,540),20)
pygame.draw.circle(tm,negro,(640,540),20,3)
#4
pygame.draw.circle(tm,blanco,(640,600),20)
pygame.draw.circle(tm,negro,(640,600),20,3)

#Pista
pygame.draw.rect(tm,blanco,(40,230,720,240))
pygame.draw.rect(tm,blanco,(230,40,340,620))
pygame.draw.rect(tm,azul,(103.34,310,126.66,80))
pygame.draw.rect(tm,azul,(103.34,230,63.34,80))
pygame.draw.rect(tm,verde,(570,310,126.68,80))
pygame.draw.rect(tm,verde,(633.34,390,63.34,80))
pygame.draw.rect(tm,rojo,(343.34,470,113.33,126.68))
pygame.draw.rect(tm,rojo,(230,533.34,113.33,63.34))
pygame.draw.rect(tm,amarillo,(343.33,103.34,113.33,126.68))
pygame.draw.rect(tm,amarillo,(456.67,103.34,113.33,63.34))
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
#1
pygame.draw.circle(tm,rojo,(160,540),10)
pygame.draw.circle(tm,negro,(160,540),10,2)
#2
pygame.draw.circle(tm,rojo,(160,600),10)
pygame.draw.circle(tm,negro,(160,600),10,2)
#3
pygame.draw.circle(tm,rojo,(100,540),10)
pygame.draw.circle(tm,negro,(100,540),10,2)
#4
pygame.draw.circle(tm,rojo,(100,600),10)
pygame.draw.circle(tm,negro,(100,600),10,2)

#azul
#1
pygame.draw.circle(tm,azul,(azul1),10)
pygame.draw.circle(tm,negro,(azul1),10,2)
#2
pygame.draw.circle(tm,azul,(azul2),10)
pygame.draw.circle(tm,negro,(azul2),10,2)
#3
pygame.draw.circle(tm,azul,(azul3),10)
pygame.draw.circle(tm,negro,(azul3),10,2)
#4
pygame.draw.circle(tm,azul,(azul4),10)
pygame.draw.circle(tm,negro,(azul4),10,2)

#amarillo
#1
pygame.draw.circle(tm,amarillo,(700,100),10)
pygame.draw.circle(tm,negro,(700,100),10,2)
#2
pygame.draw.circle(tm,amarillo,(700,160),10)
pygame.draw.circle(tm,negro,(700,160),10,2)
#3
pygame.draw.circle(tm,amarillo,(640,100),10)
pygame.draw.circle(tm,negro,(640,100),10,2)
#4
pygame.draw.circle(tm,amarillo,(640,160),10)
pygame.draw.circle(tm,negro,(640,160),10,2)

#verde
#1
pygame.draw.circle(tm,verde,(700,540),10)
pygame.draw.circle(tm,negro,(700,540),10,2)
#2
pygame.draw.circle(tm,verde,(700,600),10)
pygame.draw.circle(tm,negro,(700,600),10,2)
#3
pygame.draw.circle(tm,verde,(640,540),10)
pygame.draw.circle(tm,negro,(640,540),10,2)
#4
pygame.draw.circle(tm,verde,(640,600),10)
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
pygame.draw.line(tm,negro,(230,103.34),(570,103.34),3)
pygame.draw.line(tm,negro,(230,166.68),(570,166.68),3)
pygame.draw.line(tm,negro,(230,533.34),(570,533.34),3)
pygame.draw.line(tm,negro,(230,596.68),(570,596.68),3)
pygame.draw.line(tm,negro,(633.34,230),(633.34,470),3)
pygame.draw.line(tm,negro,(696.68,230),(696.68,470),3)
pygame.draw.line(tm,negro,(103.34,230),(103.34,470),3)
pygame.draw.line(tm,negro,(166.68,230),(166.68,470),3)


#diagonales
pygame.draw.line(tm,negro,(343.34,230),(230,166.68),3)
pygame.draw.line(tm,negro,(230,166.68),(343.34,103.34),3)
pygame.draw.line(tm,negro,(343.34,103.34),(230,40),3)
pygame.draw.line(tm,negro,(456.68,103.34),(570,40),3)
pygame.draw.line(tm,negro,(456.68,103.34),(570,166.68),3)
pygame.draw.line(tm,negro,(570,166.68),(456.668,230),3)
pygame.draw.line(tm,negro,(570,310),(456.668,230),3)
pygame.draw.line(tm,negro,(570,310),(633.348,230),3)
pygame.draw.line(tm,negro,(633.348,230),(696.68,310),3)
pygame.draw.line(tm,negro,(696.68,310),(760,230),3)
pygame.draw.line(tm,negro,(760,470),(696.68,390),3)
pygame.draw.line(tm,negro,(696.68,390),(633.34,470),3)
pygame.draw.line(tm,negro,(633.34,470),(570,390),3)
pygame.draw.line(tm,negro,(570,390),(456.68,470),3)
pygame.draw.line(tm,negro,(456.68,470),(570,533.34),3)
pygame.draw.line(tm,negro,(570,533.34),(456.68,596.68),3)
pygame.draw.line(tm,negro,(456.68,596.68),(570,660),3)
pygame.draw.line(tm,negro,(230,660),(343.34,596.68),3)
pygame.draw.line(tm,negro,(343.34,596.68),(230,533.34),3)
pygame.draw.line(tm,negro,(230,533.34),(343.34,470),3)
pygame.draw.line(tm,negro,(343.34,470),(230,390),3)
pygame.draw.line(tm,negro,(230,390),(166.68,470),3)
pygame.draw.line(tm,negro,(166.68,470),(103.34,390),3)
pygame.draw.line(tm,negro,(103.34,390),(40,470),3)
pygame.draw.line(tm,negro,(40,230),(103.34,310),3)
pygame.draw.line(tm,negro,(103.34,310),(166.68,230),3)
pygame.draw.line(tm,negro,(166.68,230),(230,310),3)
pygame.draw.line(tm,negro,(230,310),(343.34,230),3)
pygame.draw.line(tm,negro,(40,350),(103.34,350),3)
pygame.draw.line(tm,negro,(135.01,310),(135.01,390),3)
pygame.draw.line(tm,negro,(198.34,310),(198.34,390),3)
pygame.draw.line(tm,negro,(760,350),(696.68,350),3)
pygame.draw.line(tm,negro,(665.01,310),(665.01,390),3)
pygame.draw.line(tm,negro,(601.67,310),(601.67,390),3)
pygame.draw.line(tm,negro,(400,660),(400,596.67),3)
pygame.draw.line(tm,negro,(343.33,565.01),(456.67,565.01),3)
pygame.draw.line(tm,negro,(343.33,501.67),(456.67,501.67),3)
pygame.draw.line(tm,negro,(400,660),(400,596.67),3)
pygame.draw.line(tm,negro,(400,40),(400,103.34),3)
pygame.draw.line(tm,negro,(343.33,135.01),(456.67,135.01),3)
pygame.draw.line(tm,negro,(343.33,198.35),(456.67,198.35),3)


while True:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type==pygame.KEYUP:
            fuente=pygame.font.Font(None,30)
            text=fuente.render("Cayó: "+str(dado()),0,(0,0,0))
            tm.blit(text,(780,350))
        elif evento.type==pygame.KEYDOWN:
            pygame.draw.rect(tm,fondo,(780,350,80,100))

    print(pygame.mouse.get_pos())
    pygame.display.update()

