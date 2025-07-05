import pgzrun

def draw():
    screen.fill((255,255,255))
    screen.draw.text('Hello World',topleft=(10,10),fontsize=30,color='Red')
    screen.draw.text('Hello World',center=(200,150),fontsize=40,color='Green')
    screen.draw.text('Hello World',topleft=(390,270),fontsize=30,color='blue')

WIDTH = 800
HEIGHT = 500
TITLE = 'HELLO WORLD'

pgzrun.go()
