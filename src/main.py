import pygame as pg
import sys

from snake import snake_anim
from fetch import getContributionsCalendar

import logging

if __name__ == '__main__':
    logging.basicConfig(filename='snake.log', level=logging.DEBUG)
    anim = snake_anim(getContributionsCalendar())
    anim.run()