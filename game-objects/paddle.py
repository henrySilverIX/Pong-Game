from turtle import Turtle

MAX_LIMIT_Y = 245



class Paddle(Turtle):
    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.penup()
        self.goto(x_cor, y_cor)
        self.color("white")
        self.shape("square")

        #All turtles have a size of 20 by 20
        self.shapesize(stretch_wid=5, stretch_len=1)

    def go_up(self):
        if self.ycor() < MAX_LIMIT_Y:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def go_down(self):
        if self.ycor() > -MAX_LIMIT_Y:
            new_y = self.ycor()-20
            self.goto(self.xcor(), new_y)