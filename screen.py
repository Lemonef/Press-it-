import turtle
from game import Game

class ScreenHandler:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.title("Press It")
        self.screen.bgcolor("black")
        self.screen.setup(width=800, height=600)
        self.screen.tracer(0)
        
        self.start_button = None
        self.info = None
        self.info = turtle.Turtle()
        self.info.hideturtle()
        self.info.penup()
        self.info.color("white")
        self.high_score = 0
        
    def start_screen(self, click_start):
        self.clear_screen()
        self.create_start_button()
        self.screen.bgcolor("black")
        self.info.goto(0, 80)
        self.info.write( 
                "Welcome to the Press It!\n\n"
                "Press 'a', 's', 'd' when the falling balls\n"
                "reach the paddles at the bottom.\n"
                "Press at the correct timing to score.\n\n"
                "Click the start button below to begin.",
                align="center", font=("Arial", 18, "normal"))
        
          
        self.start_button.clear()
        self.start_button.penup()
        self.start_button.goto(0, -50)
        self.start_button.shape("square")
        self.start_button.color("green")
        self.start_button.shapesize(stretch_wid=2, stretch_len=5)
        self.start_button.showturtle()
        self.write_text("START", 0, -50) 
        
        self.screen.onscreenclick(lambda x, y: click_start()
                                  if (-50 <= x <= 50 and -70 <= y <= -30)
                                  else None)

        self.screen.update()
        
    def clear_screen(self):
        self.screen.clearscreen()
        self.screen.tracer(0)
        self.info = turtle.Turtle()
        self.info.hideturtle()
        self.info.penup()
        self.info.color("white")
    
    def end_screen(self, end_score):
        self.clear_screen()
        self.screen.bgcolor("black")
        
        # Update high score if necessary
        if end_score > self.high_score:
            self.high_score = end_score
            
        self.info.goto(0,80)
        self.info.write(
            f"GAME OVER\n\nYour Score: {end_score}\nHigh Score: {self.high_score}",
            align="center", font=("Arial", 24, "bold"))
        
        
        self.create_restart_button()
        self.write_text("RESTART", 0 , -50)

        self.screen.onscreenclick(
            lambda x, y: self.start_game()
            if (-50 <= x <= 50 and -70 <= y <= -50) 
            else None)

    def create_start_button(self):
        self.start_button = turtle.Turtle()
        self.start_button.hideturtle()
        self.start_button.penup()
    
    def create_restart_button(self):
        self.restart_button = turtle.Turtle()
        self.restart_button.hideturtle()
        self.restart_button.penup()
        self.restart_button.goto(0, -50)
        self.restart_button.shape("square")
        self.restart_button.color("red")
        self.restart_button.shapesize(stretch_wid=2, stretch_len=5)
        self.restart_button.showturtle()
        
    def write_text(self, text, x, y, font_size=18):
        text_turtle = turtle.Turtle()
        text_turtle.hideturtle()
        text_turtle.penup()
        text_turtle.color("white")
        text_turtle.goto(x, y)
        text_turtle.write(text, align="center",
                          font=("Arial", font_size,
                                "normal"))
        
    def start_game(self):
        self.clear_screen()
        self.create_start_button()
        self.game = Game(self.screen, self.end_game_callback)
        self.game.run() 
    
    def end_game_callback(self, end_score):
        self.end_screen(end_score)
