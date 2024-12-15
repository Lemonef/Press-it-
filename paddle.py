import turtle

class Paddle:

    def __init__(self, x, key, color="blue"):
        self.key = key
        self.x = x
        self.shape = turtle.Turtle()
        self.shape.shape("square")
        self.shape.color(color)
        self.shape.shapesize(stretch_wid=1, stretch_len=5)
        self.shape.penup()
        self.shape.goto(x, -250)
        
    def hide(self):
        self.shape.hideturtle()