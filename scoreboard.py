from turtle import Turtle


FONT = ("Courier", 24, "normal")
ALIGNMENT = 'center'


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color('white')
        self.pu()
        self.hideturtle()
        self.goto(-200, 250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Level {self.level}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over!!!\nYou you made it to level {self.level}", move=False, align=ALIGNMENT, font=FONT)

    def increase_level(self):
        self.clear()
        self.level += 1
        self.update_scoreboard()




