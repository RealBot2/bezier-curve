import sys
import pygame as pg
import copy
import math

from Point import Point
from Bezier import Bezier


pg.init()
window = pg.display.set_mode((1280, 720))
clock = pg.time.Clock()


########################################################
#setup() runs only once when program begins
def setup():
    global button_is_clicked
    global button_is_pressed
    button_is_clicked = False
    button_is_pressed = False

    global red
    global green
    red = (255, 0, 0)
    green = (0, 255, 0)

    global bezier
    global mouse_point
    bezier = Bezier(window)
    mouse_point = Point(pg.mouse.get_pos())


#loop() runs in loop until program ends
def loop():
    global button_is_clicked
    global button_is_pressed
    global mouse_point
    mouse_point.position = pg.mouse.get_pos()
    button_is_pressed = pg.mouse.get_pressed()[0]

    #update bezier points based on mouse input
    mouse_clicked_on_object = bezier.updatePosition(mouse_point, button_is_clicked, button_is_pressed)

    #if mouse clicked on background, add another point to bezier curve
    if (not mouse_clicked_on_object) and button_is_clicked:
        bezier.addPoint(Point(pg.mouse.get_pos()))
        button_is_clicked = False
    
    bezier.draw()

########################################################


#runs in at begining of loop
def doOnBeginningOfLoop():
    global mouse_point
    mouse_point.position = pg.mouse.get_pos()
    global button_is_clicked
    button_is_clicked = False

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit(0)
        if event.type == pg.MOUSEBUTTONDOWN:
            button_is_clicked = pg.mouse.get_pressed()[0]

#runs in at end of loop
def doOnEndOfLoop():
    pg.display.update()
    clock.tick(60)
    window.fill((0, 0, 0))


setup()
while True:
    doOnBeginningOfLoop()
    loop()
    doOnEndOfLoop()



