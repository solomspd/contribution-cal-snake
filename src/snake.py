from turtle import position
import pygame as pg
import numpy as np
from itertools import product, repeat
from bisect import bisect_left
import logging


class snake:
    def __init__(
        self, color=(0, 0, 255), block_size=20, bounds=(52, 7), tile_gap=2
    ):
        self.body = list(repeat((tile_gap, tile_gap), 1))
        self.block_size = block_size
        self.bounds = bounds
        self.tile_gap = tile_gap
        self.head = [0, 0]
        self.colors = [color]

    def move(self, direction):
        if direction == "U":
            dir_ammount = (0, -(self.block_size + self.tile_gap))
            self.head[1] -= 1
        elif direction == "D":
            dir_ammount = (0, self.block_size + self.tile_gap)
            self.head[1] += 1
        elif direction == "L":
            dir_ammount = (-(self.block_size + self.tile_gap), 0)
            self.head[0] -= 1
        elif direction == "R":
            dir_ammount = (self.block_size + self.tile_gap, 0)
            self.head[0] += 1
        
        tail = self.body.pop(0)
        if self.body == 0:
            self.body.append((tail[0] + dir_ammount[0], tail[1] + dir_ammount[1]))
        else:
            self.body.append((self.body[-1][0] + dir_ammount[0], self.body[-1][1] + dir_ammount[1]))

    def draw(self, screen):
        for element, i in self.body:
            pg.draw.rect(
                screen, self.colors[i], (*element, self.block_size, self.block_size), 0, 4
            )

    def eat(self, color):
        self.body.insert(0, position)
        self.colors.append(color)


class snake_anim:
    def __init__(self, commit_cal):
        pg.init()
        pg.display.set_caption("Contributions Snake")
        self.background_color = pg.Color("black")
        self.colors = [
            pg.Color(i) for i in ["#2d333b", "#0e4429", "#006d32", "#26a641", "#39d353"]
        ]
        self.tiles = commit_cal
        mx = max(map(max, self.tiles))
        mn = max(map(min, self.tiles))
        bounds = np.linspace(mn, mx, len(self.colors))

        for i in range(len(self.tiles)):
            for j in range(len(self.tiles[i])):
                self.tiles[i][j] = self.colors[
                    min(bisect_left(bounds, self.tiles[i][j]), len(self.colors) - 1)
                ]
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
            self.snake.move(self.moves[i])
            snake_head = self.snake.head
            if self.tiles[snake_head[0]][snake_head[1]] != self.colors[0]:
                self.snake.eat(self.tiles[snake_head[0]][snake_head[1]])
                self.tiles[snake_head[0]][snake_head[1]] = self.colors[0]
            self.draw()
            self.clock.tick(5)
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
