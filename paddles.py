import turtle


class Pong(turtle.Turtle):
    def __init__(self, xcor):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.shapetransform()
        self.penup()
        self.goto(xcor, 0)
        self.color("white")
        self.left(90)

    def go_up(self):
        if self.ycor() > 220:
            pass
        else:
            self.forward(20)

    def go_down(self):
        if self.ycor() < -215:
            pass
        else:
            self.backward(20)
