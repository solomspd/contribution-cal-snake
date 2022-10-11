import pygame as pg
import numpy as np
import sys
import time
import random

from itertools import product, repeat


class snake:
    def __init__(
        self, length=4, color=(0, 0, 255), block_size=20, bounds=(52, 7), tile_gap=2
    ):
        self.body = list(repeat((0, 0), length))
        self.color = color
        self.size = length
        self.block_size = block_size
        self.bounds = bounds

    def move(self, direction):
        self.body.pop(0)
        # TODO: check
        self.body.append(
            (self.body[-1][0] + direction[0], self.body[-1][1] + direction[1])
        )

    def draw(self, screen):
        for i in self.body:
            pg.draw.rect(
                screen, self.color, (*i, self.block_size, self.block_size), 0, 4
            )


class snake_anim:
    def __init__(self, commit_cal):
        pg.init()
        pg.display.set_caption("Contributions Snake")
        self.background_color = pg.Color("black")
        self.tile_color = pg.Color("green")
        self.tile_size = 20
        self.tile_gap = 2
        self.cal_size = self.cal_width, self.cal_height = 53, 7
        self.screen_size = self.screen_width, self.screen_height = (
            self.tile_gap + self.cal_width * (self.tile_size + self.tile_gap),
            self.tile_gap + self.cal_height * (self.tile_size + self.tile_gap),
        )
        self.screen = pg.display.set_mode((self.screen_size[0], self.screen_size[1]))
        self.tiles = commit_cal
        self.snake = snake(block_size=self.tile_size, tile_gap=self.tile_gap)
        self.clock = pg.time.Clock()

    def run(self):
        complete = False
        while not complete:
            # for event in pg.event.get():
            #    if event.type == pg.QUIT:
            #        pg.quit()
            #        quit()
            self.snake.move([20, 0])
            self.draw()
            self.clock.tick(30)

    def draw(self):
        self.screen.fill(self.background_color)

        x = self.tile_gap
        for i in self.tiles:
            y = self.tile_gap
            for j in i:
                pg.draw.rect(
                    self.screen,
                    j,
                    (x, y, self.tile_size, self.tile_size),
                    0,
                    4,
                )
                y += self.tile_size + self.tile_gap
            x += self.tile_size + self.tile_gap

        self.snake.draw(self.screen)
        pg.display.update()
