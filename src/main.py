import os

from snake import snake_anim
from fetch import getContributionsCalendar

import logging

if __name__ == "__main__":
    try:
        os.environ["DISPLAY"]
    except:
        os.environ["SDL_VIDEODRIVER"] = "dummy"
    logging.basicConfig(filename="snake.log", level=logging.DEBUG)
    anim = snake_anim(getContributionsCalendar())
    anim.run()
