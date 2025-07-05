import pgzrun
from random import randint
def draw():
    screen.fill('green')
    fox.draw()
    coin.draw()
    screen.draw.text("Score:"+str(score),color='black',topleft=(10,10))
    if game_over:
        screen.fill('red')
        message = "Final Score : " + str(score)
        screen.draw.text(message, topleft=(300,10),fontsize=50)

def place_coin():
    coin.x = randint(20, (WIDTH-20))
    coin.y = randint(20, (HEIGHT-20))
    
def update():
    global score
    if keyboard.left:
        fox.x = fox.x - 2
    elif keyboard.right:
        fox.x = fox.x + 2
    elif keyboard.up:
        fox.y = fox.y - 2
    elif keyboard.down:
        fox.y = fox.y + 2
        coin_collected = fox.colliderect(coin)
        if coin_collected:
            place_coin()
            score = score +1

def time_up():
    global game_over
    game_over = True
    print("Time Out")

WIDTH = 800
HEIGHT = 600

fox = Actor('fox')
fox.pos = 100,100
coin = Actor('coin')
place_coin()
score = 0
game_over = False
clock.schedule(time_up,10.0)
pgzrun.go()