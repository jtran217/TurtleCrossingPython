from turtle import Turtle
FONT = ("Courier", 24, "normal")
#This class keeps track of all things related to the scoreboard. This includes displaying,updating, increasing diffifulty and determine when game is over.


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280,250)
        self.update_scoreboard()
    def update_scoreboard(self):
        self.clear()
        self.write(f"Level:{self.level} ", align='left', font=FONT)
    def increase_level(self):
        self.level += 1
        self.update_scoreboard()
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align= 'center', font = FONT)
