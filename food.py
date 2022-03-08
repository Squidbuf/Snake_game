from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.pu()
        self.shapesize(0.5, 0.5)
        self.color("red")
        self.speed(9)
        self.refresh()

    def refresh(self):
        x_posi = random.randint(-270, 270)
        y_posi = random.randint(-270, 270)
        self.goto(x_posi, y_posi)


