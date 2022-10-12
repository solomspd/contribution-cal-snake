import pygame as pg
import numpy as np
from itertools import product, repeat
from bisect import bisect_left


class snake:
    def __init__(
        self, length=1, color=(0, 0, 255), block_size=20, bounds=(52, 7), tile_gap=2
    ):
        self.body = list(repeat((tile_gap, tile_gap, color), length))
        self.size = length
        self.block_size = block_size
        self.bounds = bounds
        self.tile_gap = tile_gap

    def move(self, direction):
        tail = self.body.pop(0)
        if direction == "U":
            dir_ammount = (0, -(self.block_size + self.tile_gap))
        elif direction == "D":
            dir_ammount = (0, self.block_size + self.tile_gap)
        elif direction == "L":
            dir_ammount = (-(self.block_size + self.tile_gap), 0)
        elif direction == "R":
            dir_ammount = (self.block_size + self.tile_gap, 0)

        if len(self.body) == 0:
            new_index = (tail[0] + dir_ammount[0], tail[1] + dir_ammount[1])
            self.body.append(new_index)
        else:
            new_index = (
                self.body[-1][0] + dir_ammount[0],
                self.body[-1][1] + dir_ammount[1],
            )
            self.body.append(new_index)
        return new_index

    def draw(self, screen):
        for element in self.body:
            pg.draw.rect(
                screen, element[2], (element[0], element[1], self.block_size, self.block_size), 0, 4
            )

    def eat(self, index, color):
        self.body.insert(0, (index[0], index[1], color))
        self.size += 1


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
        matrix = [[0] * 52] * 7
        self.generateSpiralOrder(matrix, "R")
        for i in range(len(self.moves)):
            new_index = self.snake.move(self.moves[i])
            self.snake.eat(new_index, self.tile_color)
            self.tiles[new_index[1]][new_index[0]] = self.snake.color
            self.draw()
            self.clock.tick(30)
        pg.quit()
        quit()

    def generateSpiralOrder(self, matrix, direction):
        if not matrix:
            return
        row = list(matrix.pop(0))
        if direction == "R":
            self.moves.extend(["R"] * len(row))
            self.generateSpiralOrder(([*zip(*matrix)][::-1]), "D")
        if direction == "L":
            self.moves.extend(["L"] * len(row))
            self.generateSpiralOrder(([*zip(*matrix)][::-1]), "U")
        if direction == "U":
            self.moves.extend(["U"] * len(row))
            self.generateSpiralOrder(([*zip(*matrix)][::-1]), "R")
        if direction == "D":
            self.moves.extend(["D"] * len(row))
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
