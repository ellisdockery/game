import pgzrun
from pygame.locals import *

TITLE = "Zelda Classic - PyGame Zero"
link = Actor('link_down1.png', (350, 350))
link.orientation = 'down'
link.attack = False
link.step = '1'
link.in_motion = False
link.hurt = False
#meanie = Actor('meanie_left1.png', (550, 350))
#meanie.orientation = 'right'
#meanie.initial_x = meanie.x
#meanie.step = '1'
SPEED = 5
# Play the theme music
#music.play("overworld.ogg")
# Sets the appropriate image for Link
# according to which direction he is facing
def set_link_image():
    if link.attack == True:
        link.image = 'attack_' + link.orientation
        link.attack = False
    else:
        link.image = 'link_' + link.orientation + link.step


def link_motion():
    if link.in_motion:
        if link.step == '1':
            link.step = '2'
        else:
            link.step = '1'

#def set_meanie_image():
#    meanie.image = 'meanie_' + meanie.orientation + meanie.step

#def meanie_steps():
#    if meanie.step == '1':
#        meanie.step = '2'
#    else:
#        meanie.step = '1'

# Cause meanie to pace back and forth
'''def meanie_motion():
    if meanie.orientation == 'right' and meanie.x < meanie.initial_x + 50:
        meanie.x += SPEED/2
    elif meanie.orientation == 'right' and meanie.x == meanie.initial_x + 50:
        meanie.orientation = 'left'
        meanie.x -= SPEED/2
    elif meanie.orientation == 'left' and meanie.x > meanie.initial_x - 50:
        meanie.x -= SPEED/2
    elif meanie.orientation == 'left' and meanie.x == meanie.initial_x - 50:
        meanie.orientation = 'right'
        meanie.x += SPEED/2'''
# Listens for certain keyboard events
# and updates certain object attributes
def get_keyboard(SPEED):
    if keyboard.left:
        link.orientation = 'left'
        link.x -= SPEED
        link.in_motion = True
    elif keyboard.right:
        link.orientation = 'right'
        link.x += SPEED
        link.in_motion = True
    elif keyboard.up:
        link.orientation = 'up'
        link.y -= SPEED
        link.in_motion = True
    elif keyboard.down:
        link.orientation = 'down'
        link.y += SPEED
        link.in_motion = True
    elif keyboard.a:
        link.attack = True
        sounds.sword.play()
    else:
        link.in_motion = False
# Get user input (as the name suggests)
def get_user_input():
    get_keyboard(SPEED)
# Update the game's state
def update():
    get_user_input()
    link_motion()
#    meanie_motion()
#    meanie_steps()
    set_link_image()
#    set_meanie_image()
# Draw to the screen
def draw():
    screen.blit('overworld.png', (0, 0))
    link.draw()
#    meanie.draw()

pgzrun.go()