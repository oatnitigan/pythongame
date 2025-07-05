import pgzrun
from random import randint

def draw():
    apple.draw()

def place_apple():
    apple.x = randint(10,600)
    apple.y = randint(10,400)
    
def on_mouse_down(pos):
    if apple.collidepoint(pos):
        sounds.click.play()
        place_apple()
    else:
        print("You Missed!")

WIDHT = 640
HEIGHT = 480
apple = Actor('apple')
place_apple()
pgzrun.go()