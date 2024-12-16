import turtle

class Button:
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.location = [0,0]
        self.color = color
        self.button = turtle.Turtle()
        self.button.penup()
        self.button.setheading(0)
        self.button.hideturtle()
    
    def set_location(self, location):
        self.location = location
        self.button.goto(self.location[0], self.location[1])

    def draw_button(self, message):
        self.button.color(self.color)
        self.button.penup()
        
        # Draw the rectangle
        self.button.goto(self.location[0] - self.width / 2, self.location[1] - self.height / 2)
        self.button.begin_fill()
        for _ in range(2):
            self.button.forward(self.width)
            self.button.left(90)
            self.button.forward(self.height)
            self.button.left(90)
        self.button.end_fill()

        # Write text at the center of the button
        self.button.penup()
        self.button.goto(self.location[0], self.location[1] - 10)  # Adjust -10 for vertical centering
        self.button.color("white")
        self.button.write(message, align="center", font=("Arial", 15, "bold"))

    def clear(self):
        self.button.clear()
        
    def __str__(self):
        return "button"