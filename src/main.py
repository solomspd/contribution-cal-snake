import pygame as pg
import sys

from snake import snake_anim
from fetch import getContributionsCalendar

if __name__ == '__main__':
    anim = snake_anim(0, getContributionsCalendar())
    anim.run()