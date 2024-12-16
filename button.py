import turtle

class Button:
    def __init__(self, width, height, color, message, action):
        self.width = width
        self.height = height
        self.color = color
        self.message = message
        self.action = action
        self.button = turtle.Turtle()
        self.button.penup()
        self.button.hideturtle()

    def draw_button(self, x, y):
        # Draw the button
        self.button.goto(x - self.width / 2, y + self.height / 2)
        self.button.color(self.color)
        self.button.begin_fill()
        for _ in range(2):
            self.button.forward(self.width)
            self.button.right(90)
            self.button.forward(self.height)
            self.button.right(90)
        self.button.end_fill()
        # Write the message
        self.button.goto(x, y - self.height / 4)
        self.button.color("white")
        self.button.write(self.message, align="center",
                          font=("Arial", 12, "bold"))
        
    def is_clicked(self, click_x, click_y):
        left = self.button.xcor() - self.width / 2
        right = self.button.xcor() + self.width / 2
        top = self.button.ycor() + self.height / 2
        bottom = self.button.ycor() - self.height / 2
        return left <= click_x <= right and bottom <= click_y <= top     
              
    def clear(self):
        self.button.clear()
        
    def __str__(self):
        return "Button"