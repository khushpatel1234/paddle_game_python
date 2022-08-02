from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.turtlesize(stretch_wid=1, stretch_len=1)
        self.setpos(x=0, y=0)
        self.x_move = 10
        self.y_move = 10
        self.penup()

    def move(self):
        x_new = self.xcor() + self.x_move
        y_new = self.ycor() + self.y_move
        self.setpos(x_new, y_new)

    def bounce(self):
        self.y_move *= -1

    def reverse(self):
        self.x_move *= -1

    def restart(self):
        x_new = self.xcor() * 0
        y_new = self.ycor() * 0
        self.setpos(x_new,y_new)
