import pygame, sys

screen = pygame.display.set_mode((1280, 720))

while True:
    # obsługa wydarzeń
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)

    # rysowanie
    pygame.draw.rect(screen,(200,200,100),pygame.Rect(10,50,200,100))
    pygame.display.flip()

    pygame.draw.rect(screen,(100,0,250),pygame.Rect(2,30,300,500))
