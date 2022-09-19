from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(-290,260)
        self.score = 0
        self.write(f"LEVEL:{self.score}", font=FONT)


    def game_over(self):
        self.goto(-80,0)
        self.write("GAME OVER", font = FONT)

    def update_scoreboard(self):
        self.clear()
        self.write(f"LEVEL:{self.score}", font=FONT)

    def increase_level(self):
        self.score += 1
        self.update_scoreboard()