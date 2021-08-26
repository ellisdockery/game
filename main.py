import pgzrun
from pygame.locals import *
import time

WIDTH = 800
HEIGHT = 537

LINK_SPEED = 5

STEPS = '1'

link = Actor('link_right1', (WIDTH/2,HEIGHT/2))

def set_image(pos, STEPS):
    if STEPS == '1':
        STEPS = '2'
        link.image = 'link_' + pos + STEPS
        time.sleep(0.02)
    else:
        STEPS = '1'
        link.image = 'link_' + pos + STEPS
        time.sleep(0.02)

def get_keyboard():
    if keyboard.down:
        set_image('down', STEPS)
        link.y += LINK_SPEED
        print(link.image)
    elif keyboard.up:
        set_image('up', STEPS)
        link.y -= LINK_SPEED
        print(link.image)
    elif keyboard.left:
        set_image('left', STEPS)
        link.x -= LINK_SPEED
        print(link.image)
    elif keyboard.right:
        set_image('right', STEPS)
        link.x += LINK_SPEED
        print(link.image)


def update():
    get_keyboard()
def draw():
    screen.clear()
    screen.blit('overworld', (0,0))
    link.draw()

pgzrun.go()