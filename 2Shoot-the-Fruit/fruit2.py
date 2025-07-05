import pgzrun
from random import randint

# Constants for screen dimensions
WIDTH = 640
HEIGHT = 480
score = 0
# Create the apple actor
apple = Actor('apple')



def place_apple():
    """Places the apple at a random position on the screen."""
    apple.x = randint(10, 600)
    apple.y = 0
    apple.speed = randint(2,10)

def draw():
    """Draws the apple on the screen."""
    screen.clear() # Clear the screen each frame
    screen.draw.text("Score : " + str(score), topright=(630,10),fontsize=28,color="blue")
    apple.draw()

def on_mouse_down(pos):
    global score
    """Handles mouse click events."""
    if apple.collidepoint(pos):
        sounds.click.play()
        score += 1
        # When the apple is clicked, replace it
        place_apple()
    else:
        print("You Missed!")
        
def update():
    apple.y += apple.speed
    if apple.y > HEIGHT:
        place_apple()

# Initial placement of the apple when the game starts
place_apple()



# Run the game
pgzrun.go()