import pygame as pg
from copy import deepcopy

from Point import Point



class Bezier:
    point_arr = []              #array of points determining bezier curve
    prev_point_arr = []         #last array of points for which curve_points are calculated
    curve_points = []           #cached curve_points

    surface = None              #surface that curve is going to be drawn to
    max_dist = 2                #max distance between curve points

    def __init__(self, surface, max_dist = 2) -> None:
        self.surface = surface
        self.max_dist = max_dist

    def addPoint(self, point):              #add another point if there is less than 4 points allready
        if len(self.point_arr) >= 4:
            return None
        point.holding_with_mouse = True
        self.point_arr.append(point)
    
    def updatePosition(self, mouse_point, button_is_clicked, button_is_pressed) -> bool:
        if button_is_clicked:
            for point in self.point_arr:
                if point.collidesWith(mouse_point, 10):
                    point.position = mouse_point.position
                    point.holding_with_mouse = True
                    return True
        else:
            if button_is_pressed:
                for point in self.point_arr:
                    if point.holding_with_mouse:
                        point.position = mouse_point.position
                        break
                return True
            else:
                for point in self.point_arr:
                    point.holding_with_mouse = False
                return False

    def draw(self):
        red = (255, 0, 0)
        green = (0, 255, 0)

        self.drawCurve()

        for point in self.point_arr:
            color = green if point.collidesWith(Point(pg.mouse.get_pos()), 10) else red
            point.draw(self.surface, color, 10)
    
    def lerp(self, t):                  #linear interpolation of points based on parameter t
        if len(self.point_arr) == 0:
            return None
        new_arr = deepcopy(self.point_arr)

        while len(new_arr) > 1:
            for i in range(len(new_arr) - 1):
                x0 = new_arr[i].position[0]
                y0 = new_arr[i].position[1]
                x1 = new_arr[i+1].position[0]
                y1 = new_arr[i+1].position[1]

                new_x = x0 + t * (x1 - x0)
                new_y = y0 + t * (y1 - y0)
                new_point = Point((new_x, new_y))
                new_arr[i] = new_point

            new_arr.pop()
        
        return new_arr[0]
    
    def getCurvePoints(self):
        if self.point_arr == self.prev_point_arr:
            return None

        arr = []
        n = (len(self.point_arr) - 1) * 4

        for i in range(n):
            t = i / n
            point = self.lerp(t)
            point.t = t
            arr.append(point)
        
        point = self.lerp(1)
        point.t = 1
        arr.append(point)


        points_are_to_far = True

        while points_are_to_far:
            new_arr = []
            points_are_to_far = False

            for i in range(len(arr) - 1):
                new_arr.append(arr[i])
                if arr[i].distanceTo(arr[i + 1]) > self.max_dist:
                    t = (arr[i].t + arr[i + 1].t) / 2
                    point = self.lerp(t)
                    point.t = t
                    new_arr.append(point)
                    points_are_to_far = True

            new_arr.append(arr.pop())
            arr = new_arr
        
        self.curve_points = new_arr
        self.prev_point_arr = deepcopy(self.point_arr)

    
    def drawCurve(self):
        self.getCurvePoints()

        color = (128, 128, 128)
        line_width = 2
        for i in range(len(self.curve_points) - 1):
            pg.draw.line(self.surface, color, self.curve_points[i].position, self.curve_points[i + 1].position, line_width)





