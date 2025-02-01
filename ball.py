import turtle
import random
start_angle = random.randint(30, 60)


class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.x = 10
        self.y = 10
        self.speed_pos = 0.09

    def start(self):
        nx = self.xcor() + self.x
        ny = self.ycor() + self.y
        self.goto(nx, ny)

    def bounce_y(self):
        self.y *= -1
        self.start()

    def bounce_x(self):
        self.x *= -1
        self.speed_pos *= 0.9
        self.start()

    def reset_position(self):
        self.goto(0, 0)
        self.speed_pos = 0.1
        self.bounce_x()
