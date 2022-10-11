import pygame as pg
import numpy as np
import sys
import time
import random

from itertools import product, repeat


class snake:
    def __init__(self, length=4, color=(0, 0, 255), block_size=20, bounds=(52,7)):
        self.body = list(repeat((0,0), length))
        self.color = color
        self.size = length
        self.block_size = block_size
        self.bounds = bounds
    
    def move(self, direction):
        self.body.pop()
        # TODO: check
        self.body.append((self.body[-1][0] + direction[0], self.body[-1][1] + direction[1]))

    def draw(self, screen):
        for i in self.body:
            pg.draw.rect(
                screen, self.color, (*i, self.block_size, self.block_size), 0, 4
            )


class snake_anim:
    def __init__(self, commit_cal):
        pg.init()
        self.background_color = pg.Color("black")
        self.tile_color = pg.Color("green")
        self.tile_size = 20
        self.tile_gap = 2
        self.cal_size = self.cal_width, self.cal_height = 52, 7
        self.screen_size = self.screen_width, self.screen_height = (
            self.tile_gap + self.cal_width * (self.tile_size + self.tile_gap),
            self.tile_gap + self.cal_height * (self.tile_size + self.tile_gap),
        )
        self.screen = pg.display.set_mode(self.screen_size)
        # self.tile_color = np.zeros(self.cal_size)
        self.tiles = product(
            range(self.tile_gap, self.screen_width, self.tile_size + self.tile_gap),
            range(self.tile_gap, self.screen_height, self.tile_size + self.tile_gap),
        )
        self.snake = snake(block_size=self.tile_size)

    def run(self):
        complete = False
        while not complete:
            # for event in pg.event.get():
            #     if event.type == pg.QUIT:
            #         pg.quit()
            #         sys.exit()
            self.snake.move(random.choice([(-1, 0), (1, 0), (0, -1), (0, 1)]))
            self.draw()
            time.sleep(0.5)

    def draw(self):
        # self.screen.fill(self.background_color)
        for i in self.tiles:
            pg.draw.rect(
                self.screen, self.tile_color, (*i, self.tile_size, self.tile_size), 0, 3
            )
        self.snake.draw(self.screen)
        pg.display.update()
        # pg.display.flip()
