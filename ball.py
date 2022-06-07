from turtle import Turtle
import time

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.goto(0, 0)
        self.x_move = 10
        self.y_move = 10
        self.speed_level = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    # def speed_up(self):
    #     self.speed_level -= 0.01
    #     time.sleep(self.speed_level)
    #     if self.speed_level <= 0.01:
    #         self.speed_level = 0.01

    def bounce_y(self):
        self.y_move *= -1
        self.speed_level *= 0.9
        if self.speed_level <= 0.01:
            self.speed_level = 0.01

    def bounce_x(self):
        self.x_move *= -1
        self.speed_level *= 0.9
        if self.speed_level <= 0.01:
            self.speed_level = 0.01

    def reset(self):
        self.goto(0, 0)
        self.speed_level = 0.1
        self.bounce_x()
