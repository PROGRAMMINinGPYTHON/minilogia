import pygame, sys, os
from pygame.locals import *

pygame.init()
widow = pygame.display.set_mode((720, 480))
pygame.display.set_caption("nazwa_okna")
moja_grafika = pygame.image.load('green-car2.png')
screen = pygame.display.get_surface()
screen.blit(moja_grafika,(0,0))
pygame.display.flip()
def xxxx(events):#xxxx = input
    for event in events:
        if event.type == QUIT:
            sys.exit(0)
        else:
            print(event)
while True:
    xxxx(pygame.event.get())

