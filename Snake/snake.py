import turtle
from turtle import Turtle

Starting_positions = [(0, 0), (-20, 0), (-40, 0)]
move_distance = 20
up = 90
down = 270
left = 180
right = 0

class Snake():

    def __init__(self):
        self.start_snake = []
        self.create_snake()
        self.head = self.start_snake[0]
        self.head_mod()

    def create_snake(self):
        for cubes in Starting_positions:
            self.add_segment(cubes)

    def add_segment(self, cubes):
        snake = Turtle(shape="square")
        snake.color("green")
        snake.shapesize(0.5, 0.5)
        snake.penup()
        snake.goto(cubes)
        self.start_snake.append(snake)


    def extend(self):
        self.add_segment(self.start_snake[-1].position())

    def head_mod(self):
        self.head.color("white")
        self.head.shape("circle")
        self.head.shapesize(0.6, 0.8)

    def move(self):
        for snakes in range(len(self.start_snake) - 1, 0, -1):
            new_x = self.start_snake[snakes - 1].xcor()
            new_y = self.start_snake[snakes - 1].ycor()
            self.start_snake[snakes].goto(new_x, new_y)
        self.head.forward(move_distance)

    def up(self):
        if self.head.heading() != down:
            self.head.setheading(up)
    def down(self):
        if self.head.heading() != up:
            self.head.setheading(down)
    def left(self):
        if self.head.heading() != right:
            self.head.setheading(left)
    def right(self):
        if self.head.heading() != left:
            self.head.setheading(right)