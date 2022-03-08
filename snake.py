from turtle import Turtle
import random

DISTANCE = [(0, 0) , (0, 0), (0, 0)]
MOVE_DIS = 20
MOVE_DIR = 90
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]

    def create_snake(self):
        for position in DISTANCE:
            self.add_segment(position)

    def add_segment(self, position):
        shabu = Turtle("square")
        shabu.color("white")
        shabu.pu()
        shabu.goto(position)
        self.segment.append(shabu)



    def extend(self):
        self.add_segment(self.segment[-1].position())

    def move(self):
        for seg in range(len(self.segment) - 1, 0, -1):
            x_posi = self.segment[seg - 1].xcor()
            y_posi = self.segment[seg - 1].ycor()
            self.segment[seg].goto(x_posi, y_posi)
        self.head.fd(MOVE_DIS)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
