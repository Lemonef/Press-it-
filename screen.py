import turtle
from game import Game
from button import Button

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
        self.create_button("START", 0, -80, "green", click_start)
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
        self.create_button("RESTART", 0, -80, "red", self.start_game)
        self.screen.update()
        
    def  create_button(self, message, x, y, color, click_callback):
        self.button = Button(200, 50, color)
        self.button.draw_button(message)
        self.button.set_location([x, y])
        
        # Add click event
        self.screen.onscreenclick(lambda x, y: click_callback()
                                  if (x - 50 <= x <= x + 50 and y - 20 <= y <= y + 20)
                                  else None)
        
    def clear_screen(self):
        self.screen.clearscreen()
        self.screen.tracer(0)
        self.info = turtle.Turtle()
        self.info.hideturtle()
        self.info.penup()
        self.info.color("white")
    
    def start_game(self):
        self.clear_screen()
        self.game = Game(self.screen, self.end_game_callback)
        self.game.run()
        
    def end_game_callback(self, end_score):
        self.end_screen(end_score)
