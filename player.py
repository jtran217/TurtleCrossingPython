from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
#This class is responsible for generating the player object and positioning them at the starting line.

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('black')
        self.penup()
        self.go_to_start()
        self.setheading(90)
    def move(self):
        self.forward(MOVE_DISTANCE)
    def reset(self):
        self.reset()
        self.goto(STARTING_POSITION)
        self.setheading(90)
    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
    def go_to_start(self):
        self.goto(STARTING_POSITION)






