import pygame as pg
import numpy as np
from itertools import product, repeat
from bisect import bisect_left


class snake:
    def __init__(
        self, length=4, color=(0, 0, 255), block_size=20, bounds=(52, 7), tile_gap=2
    ):
        self.body = list(repeat((tile_gap, tile_gap), length))
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
        colors = [
            pg.Color(i) for i in ["#2d333b", "#0e4429", "#006d32", "#26a641", "#39d353"]
        ]
        self.tiles = commit_cal
        mx = max(map(max, self.tiles))
        mn = max(map(min, self.tiles))
        bounds = np.linspace(mn, mx, len(colors))
        
        for i in range(len(self.tiles)):
            for j in range(len(self.tiles[i])):
                self.tiles[i][j] = colors[min(bisect_left(bounds, self.tiles[i][j]), len(colors) - 1)]
        self.tile_size = 20
        self.tile_gap = 2
        self.cal_size = self.cal_width, self.cal_height = 53, 7
        self.screen_size = self.screen_width, self.screen_height = (
            self.tile_gap + self.cal_width * (self.tile_size + self.tile_gap),
            self.tile_gap + self.cal_height * (self.tile_size + self.tile_gap),
        )
        self.screen = pg.display.set_mode((self.screen_size[0], self.screen_size[1]))
        self.snake = snake(block_size=self.tile_size, tile_gap=self.tile_gap)
        self.clock = pg.time.Clock()
        self.moves = []

    def run(self):
        map = [[0] * 52] * 7
        self.generateSpiralOrder(map, "R")
        for i in range(len(self.moves)):
            self.snake.move(self.moves[i])
            self.draw()
            self.clock.tick(30)
        pg.quit()
        quit()

    def generateSpiralOrder(self, matrix, direction):
        if not matrix:
            return
        row = list(matrix.pop(0))
        if direction == "R":
            self.moves.extend([[22, 0]] * len(row))
            self.generateSpiralOrder(([*zip(*matrix)][::-1]), "D")
        if direction == "L":
            self.moves.extend([[-22, 0]] * len(row))
            self.generateSpiralOrder(([*zip(*matrix)][::-1]), "U")
        if direction == "U":
            self.moves.extend([[0, -22]] * len(row))
            self.generateSpiralOrder(([*zip(*matrix)][::-1]), "R")
        if direction == "D":
            self.moves.extend([[0, 22]] * len(row))
            self.generateSpiralOrder(([*zip(*matrix)][::-1]), "L")

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
