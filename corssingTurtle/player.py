from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def reset_position(self):
        self.goto(STARTING_POSITION)


    def player_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False


    def move(self):
        self.forward(MOVE_DISTANCE)