from turtle import Turtle
import random

BLOCK_SIZE = 20

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        # self.shapesize(stretch_wid=.5, stretch_len=.5)
        self.color("cyan")
        self.speed("fastest")
        rand_x = random.randint(-280 / BLOCK_SIZE, 280 / BLOCK_SIZE) * BLOCK_SIZE
        rand_y = random.randint(-280 / BLOCK_SIZE, 280 / BLOCK_SIZE) * BLOCK_SIZE
        self.goto(rand_x, rand_y)

    def refresh(self):
        rand_x = random.randint(-280 / BLOCK_SIZE, 280 / BLOCK_SIZE) * BLOCK_SIZE
        rand_y = random.randint(-280 / BLOCK_SIZE, 280 / BLOCK_SIZE) * BLOCK_SIZE
        self.goto(rand_x, rand_y)