from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 15
FINISH_LINE_Y = 280
UP = 90


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.pu()
        self.shape('turtle')
        self.color('white')
        self.player_reset()
        self.seth(UP)

    def move_up(self):
        self.seth(UP)
        self.forward(MOVE_DISTANCE)

    def move_down(self):
        self.seth(UP)
        self.backward(MOVE_DISTANCE)

    def move_left(self):
        self.seth(UP)
        new_xcor = self.xcor() - MOVE_DISTANCE
        self.goto(new_xcor, self.ycor())

    def move_right(self):
        self.seth(UP)
        new_xcor = self.xcor() + MOVE_DISTANCE
        self.goto(new_xcor, self.ycor())

    def player_reset(self):
        self.goto(STARTING_POSITION)

