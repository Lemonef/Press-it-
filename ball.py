import turtle

class Ball:
    def __init__(self, x, key, speed):
        self.shape = turtle.Turtle()
        self.shape.shape("circle")
        self.shape.color("red")
        self.shape.penup()
        self.shape.goto(x, 250)
        
        self.key = key
        self.active = True
        self.bouncing = False
        self.speed = speed

    def move(self):
        if self.active:
            y = self.shape.ycor()
            if self.bouncing:
                y += self.speed  # Move up when bouncing
                if y > 250:
                    self.active = False
                    self.shape.hideturtle()
                    return False  # Ball has bounced out of view
            else:
                y -= self.speed  # Move down
                if y < -300:
                    self.active = False
                    self.shape.hideturtle()
                    return False  # Ball missed
            self.shape.sety(y)
        return True

    def is_in_target_range(self):
        y = self.shape.ycor()
        return -270 <= y <= -230