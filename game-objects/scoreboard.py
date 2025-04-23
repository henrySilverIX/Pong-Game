from turtle import Turtle

ALIGNMENT = "center"
CLASS_FAMILY = "Montserrat"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0, 270)
        self.score_right = 0
        self.score_left = 0
        self.hideturtle()
        self.color("white")
        self.speed("fastest")
        self.write(f"Score:\n{self.score_left}:{self.score_right}", False, align=ALIGNMENT ,font=(CLASS_FAMILY, 8,'normal'))

    def writeScoreLeft(self):
        self.score_left += 1
        self.clear()
        self.write(f"Score:\n{self.score_left}:{self.score_right}", False, align=ALIGNMENT ,font=(CLASS_FAMILY, 8,'normal'))

    def writeScoreRight(self):
        self.score_right += 1
        self.clear()
        self.write(f"Score:\n{self.score_left}:{self.score_right}", False, align=ALIGNMENT ,font=(CLASS_FAMILY, 8,'normal'))

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(f"GAME OVER\nFinal Score: {self.score_left} : {self.score_right}", False, align=ALIGNMENT, font=(CLASS_FAMILY, 8, 'normal'))