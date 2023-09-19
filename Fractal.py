from math import cos, sin, radians
from PIL import Image, ImageDraw

class Fractal:
    def __init__(self, x0, y0, alpha, theta, len, width, image, color):
        self.x0 = x0
        self.y0 = y0
        self.x1 = x0
        self.y1 = y0
        self.alpha = alpha
        self.alpha0 = alpha
        self.theta = theta
        self.len = len
        self.width = width
        self.image = image
        self.color = color
    
    def positive(self):
        self.alpha -= self.theta
    
    def negative(self):
        self.alpha += self.theta

    def F(self):
        x2 = self.x1 + self.len * cos(radians(self.alpha))
        y2 = self.y1 + self.len * sin(radians(self.alpha))
        self.image.line([(self.x1, self.y1),(x2, y2)], self.color, width = self.width)
        self.x1 = x2
        self.y1 = y2

    def save(self):
        self.x0 = self.x1
        self.y0 = self.y1
        self.alpha0 = self.alpha
    
    def back(self):
        self.x1 = self.x0
        self.y1 = self.y0
        self.alpha = self.alpha0
    
    def print(self, rule):
        for s in rule:
            match s:
                case "F":
                    self.F()
                case "+":
                    self.positive()
                case "-":
                    self.negative()
                case "[":
                    self.save()
                case "]":
                    self.back()


