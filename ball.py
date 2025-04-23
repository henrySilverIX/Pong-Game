from turtle import Turtle

MOVE_DISTANCE = 10


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, 0)
        self.color("white")
        self.shape("circle")
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.move_speed = 0.1
        self.sinal_y = 1
        self.sinal_x = 1

    def move(self):
        new_x = self.xcor() + (self.sinal_x * MOVE_DISTANCE)
        new_y = self.ycor() + (self.sinal_y * MOVE_DISTANCE)
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.sinal_y *= -1

    def bounce_x(self):
        self.sinal_x *= -1
        self.move_speed *= 0.9


    def reset_position(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.bounce_x()
