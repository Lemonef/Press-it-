import turtle
from screen import ScreenHandler

if __name__ == "__main__":
    screen_handler = ScreenHandler()
    screen_handler.start_screen(screen_handler.start_game)
    turtle.done()
