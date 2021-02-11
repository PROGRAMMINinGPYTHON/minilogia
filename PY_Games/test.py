from pygame import *

init()

screen = display.set_mode((400,200))


display.set_caption('czy_to_zadziala')#działa
size = (50,50)
line = Surface(size)
draw.line(line,"RED",(0,0),(50,50))
Color(200,200,200)


running = True
while running:

    for event in event.get():
        if event.type == QUIT:
            running = False