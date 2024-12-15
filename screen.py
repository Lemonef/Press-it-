import turtle
from game import Game

class ScreenHandler:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.title("Press It")
        self.screen.bgcolor("black")
        self.screen.setup(width=800, height=600)
        self.screen.tracer(0)
        
        self.info = turtle.Turtle()
        self.info.hideturtle()
        self.info.penup()
        self.info.color("white")
        self.high_score = 0
        
        self.start_button = None
        self.restart_button = None
        
    def start_screen(self, click_start):
        self.clear_screen()
        self.screen.bgcolor("black")
        
        # Display instructions
        self.info.goto(0, 80)
        self.info.write(
            "Welcome to Press It!\n\n"
            "Press 'a', 's', 'd' when the falling balls\n"
            "reach the paddles at the bottom.\n"
            "Press at the correct timing to score.\n\n"
            "Click the start button below to begin.",
            align="center", font=("Arial", 18, "normal"))
        
        # Create start button
        self.create_button("START", 0, -50, "green", click_start)
        self.screen.update()
        
    def end_screen(self, end_score):
        self.clear_screen()
        self.screen.bgcolor("black")
        
        # Update high score if necessary
        if end_score > self.high_score:
            self.high_score = end_score
        
        # Display game over and scores
        self.info.goto(0, 80)
        self.info.write(
            f"GAME OVER\n\nYour Score: {end_score}\nHigh Score: {self.high_score}",
            align="center", font=("Arial", 24, "bold"))
        
        # Create restart button
        self.create_button("RESTART", 0, -50, "red", self.start_game)
        self.screen.update()
        
    def create_button(self, text, x, y, color, click_callback):
        button = turtle.Turtle()
        button.hideturtle()
        button.penup()
        button.goto(x, y)
        button.shape("square")
        button.color(color)
        button.shapesize(stretch_wid=2, stretch_len=5)
        button.showturtle()
        
        # Write text on the button
        self.write_text(text, x, y - 10, font_size=16)
        
        # Add click event
        self.screen.onscreenclick(lambda x_pos, y_pos: click_callback()
                                  if (x - 50 <= x_pos <= x + 50 and y - 20 <= y_pos <= y + 20)
                                  else None)
        
    def clear_screen(self):
        self.screen.clearscreen()
        self.screen.tracer(0)
        self.info = turtle.Turtle()
        self.info.hideturtle()
        self.info.penup()
        self.info.color("white")
    
    def write_text(self, text, x, y, font_size=18):
        text_turtle = turtle.Turtle()
        text_turtle.hideturtle()
        text_turtle.penup()
        text_turtle.color("white")
        text_turtle.goto(x, y)
        text_turtle.write(text, align="center", font=("Arial", font_size, "normal"))
        
    def start_game(self):
        self.clear_screen()
        self.game = Game(self.screen, self.end_game_callback)
        self.game.run()
        
    def end_game_callback(self, end_score):
        self.end_screen(end_score)
