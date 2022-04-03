import random
from Snake import *

DIRECTIONS = {'NORTH', 'EAST', 'SOUTH', 'WEST'}

class GameManager:
    def __init__(self, xTiles, yTiles):
        self.snake = Snake()
        self.size = (xTiles, yTiles)
        self.direction = 'EAST'
        self.newSnake()
        self.spawnFood()

    def newSnake(self):
        for i in range(1, 5):
            self.snake.eat(i, self.size[1] // 2)

    def setDirection(self, direction):
        if direction in DIRECTIONS:
            self.direction = direction
        else:
            raise Exception('Invalid direction (NORTH, EAST, SOUTH, WEST).')

    def spawnFood(self):
        x = random.randint(0, self.size[0] - 1)
        y = random.randint(0, self.size[1] - 1)
        while self.snake.contains(x, y):
            x = random.randint(0, self.size[0] - 1)
            y = random.randint(0, self.size[1] - 1)
        self.food = (x, y)

    def update(self):
        (x, y) = self.snake.head()
        if (self.direction == 'NORTH'):
            y -= 1
        elif (self.direction == 'SOUTH'):
            y += 1
        elif (self.direction == 'EAST'):
            x += 1
        else : #WEST
            x -= 1
        outOfBounds = x < 0 or y < 0 or x == self.size[0] or y == self.size[1]
        if outOfBounds or self.snake.contains(x, y):
            return False
        if (x, y) == self.food:
            self.snake.eat(x, y)
            self.spawnFood()
        else:
            self.snake.move(x, y)
        return True