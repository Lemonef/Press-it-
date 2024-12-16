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
        self.exit_button = None
        
    def start_screen(self, click_start):
        self.clear_screen()
        self.screen.bgcolor("black")
        
        # Display instructions
        self.info.goto(0, 230)
        self.info.write(
            "Welcome to Press It!",
            align="center", font=("Arial", 28, "bold"))
        
        self.info.goto(0, 120)
        self.info.write(
            "Controls:\n"
            "Press 'a' for purple\n"
            "Press 's' for yellow\n"
            "Press 'd' for blue",
            align="center", font=("Arial", 18, "normal"))
        
        self.info.goto(0, 20)
        self.info.write(
            "Objective:\n"
            "Press the correct key when the falling balls\n"
            "reach the paddles at the bottom.",
            align="center", font=("Arial", 18, "normal"))
        
        self.info.goto(0, -40)
        self.info.write(
            "Timing is key! Score as many points as you can.\n"
            "But beware of missing the target!",
            align="center", font=("Arial", 16, "italic"))
        
        self.info.goto(0, -150)
        self.info.write(
            "Click the START button below to begin the game!\n"
            "You can exit any time! Just press the EXIT button\n"
            "Try to get the highest score possible! good luck!",
            align="center", font=("Arial", 18, "bold"))
            
        # Create start button
        self.start_button = Button(200, 50, "green", "START", click_start)
        self.start_button.draw_button(0, -200)
        self.screen.update()
        self.screen.onscreenclick(self.check_start_click)
        
    def check_start_click(self, x, y):
        if self.start_button and self.start_button.is_clicked(x, y):
            self.start_button.action()
        
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
        self.restart_button = Button(200, 50, "red", "RESTART", self.start_game)
        self.restart_button.draw_button(0, -50)
        self.screen.update()
        self.screen.onscreenclick(self.check_restart_click)
        
    def check_restart_click(self, x, y):
        if self.restart_button and self.restart_button.is_clicked(x, y):
            self.restart_button.action()
        
    def clear_screen(self):
        self.screen.clearscreen()
        self.screen.tracer(0)
        self.info = turtle.Turtle()
        self.info.hideturtle()
        self.info.penup()
        self.info.color("white")
    
    def start_game(self):
        self.clear_screen()
        self.game = Game(self.screen, self.end_game_callback, self)
        self.game.run()
        
    def end_game_callback(self, end_score):
        self.end_screen(end_score)
        
    def __str__(self):
        return "Screen"