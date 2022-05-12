import sys
import pygame as pg

from Point import Point
from Bezier import Bezier


window_size = (1280, 720)
background_color = (0, 0, 0)
target_fps = 60


#### SETUP ####
pg.init()
window = pg.display.set_mode(window_size)
clock = pg.time.Clock()

button_is_clicked = False
button_is_pressed = False

red = (255, 0, 0)
green = (0, 255, 0)

bezier = Bezier(window)
mouse_point = Point(pg.mouse.get_pos())


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


def doOnBeginningOfLoop():
    global mouse_point
    mouse_point.position = pg.mouse.get_pos()
    global button_is_clicked
    button_is_clicked = False

    window.fill(background_color)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit(0)
        if event.type == pg.MOUSEBUTTONDOWN:
            button_is_clicked = pg.mouse.get_pressed()[0]


def doOnEndOfLoop():
    pg.display.update()
    clock.tick(target_fps)


while True:
    doOnBeginningOfLoop()
    loop()
    doOnEndOfLoop()



