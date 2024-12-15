import turtle
import time
import random
from paddle import Paddle
from ball import Ball

class Game:
    def __init__(self, screen, end_score_callback):
        self.screen = screen
        self.end_score_callback = end_score_callback
        
        self.screen.bgcolor("black")
        
        self.keys = ['a', 's', 'd']
        self.key_positions = {'a': -200, 's': 0, 'd': 200}
        
        # Paddle
        self.paddles = {key: Paddle(self.key_positions[key], key)
                        for key in self.keys}
        
        # Score
        self.score = 0
        self.score_display = turtle.Turtle()
        self.score_display.hideturtle()
        self.score_display.penup()
        self.score_display.color("white")
        self.score_display.goto(0, 260)
        self.update_score_display()
        self.screen.update()
        
        # Ball
        self.balls = []
        self.base_spawn_interval = 2  # seconds
        self.base_speed = 5
        self.last_spawn_time = time.time()
        
        # Key Bindings
        self.screen.listen()
        self.screen.onkey(self.press_a, 'a')
        self.screen.onkey(self.press_s, 's')
        self.screen.onkey(self.press_d, 'd')
        
    def update_score_display(self):
        self.score_display.clear()
        self.score_display.write(f"Score: {self.score}",
                                 align="center",
                                 font=("Arial", 24, "normal"))
        
    def press_a(self):
        self.check_key_press('a')
    def press_s(self):
        self.check_key_press('s')
    def press_d(self):
        self.check_key_press('d')
        
    def check_key_press(self, key):
        for ball in self.balls:  
            if ball.active and ball.key == key and ball.is_in_target_range():
                ball.bouncing = True
                ball.shape.color("White")
                self.score += 1
                self.update_score_display()
                return
        self.score -= 1
        self.update_score_display()
    
    def spawn_ball(self):
        spawn_key = random.choice(self.keys)
        x_pos = self.key_positions[spawn_key]
        speed = self.base_speed + (self.score * 0.5) if self.score > 0 else self.base_speed
        new_ball = Ball(x_pos, spawn_key, speed)
        self.balls.append(new_ball)
    
    def run(self):
        while True:
            # Calculate spawn interval
            if self.score > 0:
                # Decrease interval with score
                spawn_interval = max(0.5, self.base_spawn_interval - (self.score * 0.1))
            else:
                spawn_interval = max(0.5, self.base_spawn_interval)
                
            # Spawn ball at intervals
            current_time = time.time()
            if current_time - self.last_spawn_time >= spawn_interval:
                self.spawn_ball()
                self.last_spawn_time = current_time
            
            # Move balls
            for ball in self.balls[:]:
                if not ball.move():
                    if not ball.bouncing:
                        self.score -= 1
                        self.update_score_display()
                    self.balls.remove(ball)               
            if self.score <= -10:
                self.game_over()
                
            if self.score <= -10:
                self.game_over()
                break
            
            self.screen.update()
            time.sleep(0.05)
    
    def game_over(self):
        # Hide balls and paddles
        for ball in self.balls:
            ball.shape.clear()
        for paddle in self.paddles.values():
            paddle.hide()
        
        end_score = self.score
        self.end_score_callback(end_score)
            
        
            
        
            
            