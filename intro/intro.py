import pgzrun
import random

from pgzero.actor import Actor

alien = Actor('alien')
alien.pos = 100, 56

WIDTH = 500
HEIGHT = alien.height + 20


def draw():
    screen.clear()
    alien.draw()


pgzrun.go()
