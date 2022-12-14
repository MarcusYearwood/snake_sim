from turtle import Turtle, Screen
import time
from point import Point
from scoreboard import Scoreboard


SCREEN_HEIGHT = 600
SCREEN_WIDTH = 600
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
BLOCK_SIZE = 20


class Snake:

    global segments
    segments = []


    def __init__(self, length, screen):
        self.graphDriver = Graph(SCREEN_WIDTH, SCREEN_HEIGHT, BLOCK_SIZE)
        self.drawBorder(screen)
        for turtle in range(0, length):
            self.add_segment((turtle * BLOCK_SIZE * -1, 0))
        screen.update()
        self.head = segments[0]
        self.commandQueue = []

    #speed is time between updates (closer to 0 is faster)
    def go(self, screen, speed):
        for seg in range(0, len(segments) - 1):
            lastseg = len(segments) - 1 - seg
            segments[lastseg].goto(segments[len(segments) - 2 - seg].xcor(),
                                    segments[len(segments) - 2 - seg].ycor())
        self.listen_direction(screen)
        self.change_direction()
        self.head.forward(BLOCK_SIZE)
        screen.update()
        time.sleep(speed)

    # get next position
    def next_pos(self):
        x = head.xcor()
        y = head.ycor()
        if head.heading() == UP:
            pass

    def add_segment(self, position):
        turt = Turtle("square")
        turt.color("white")
        turt.penup()
        turt.goto(position)
        turt.resizemode("user")
        turt.shapesize(stretch_wid=.9, stretch_len=.9)
        segments.append(turt)

    def check_collision(self, food, scoreboard):
        for segment in segments[1:]:
            if self.head.distance(segment) < (BLOCK_SIZE / 2):
                scoreboard.gameoverself()
                return False
        if self.head.distance(food) < (BLOCK_SIZE / 1.5):
            food.refresh()
            scoreboard.update()
            self.add_head()
        if self.head.xcor() > (SCREEN_WIDTH / 2) - (2 * BLOCK_SIZE) \
                or self.head.ycor() > (SCREEN_HEIGHT / 2) - (2 * BLOCK_SIZE) \
                or self.head.xcor() < (SCREEN_WIDTH / -2) + (2 * BLOCK_SIZE) \
                or self.head.ycor() < (SCREEN_HEIGHT / -2) + (2 * BLOCK_SIZE):
            scoreboard.gameoverwall()
            return False
        else:
            return True

    # def check_autocanibalism(self):
    #     for segment in segments:
    #         if segment == self.head:
    #             pass
    #         elif self.head.distance(segment) < 10:
    #             scoreboard.gameover()
    #             return False

    def listen_direction(self, screen):
        screen.listen()
        screen.onkey(self.appendUp, 'Up')
        screen.onkey(self.appendDown, 'Down')
        screen.onkey(self.appendLeft, 'Left')
        screen.onkey(self.appendRight, 'Right')

    def appendUp(self):
        self.commandQueue.append('up')

    def appendDown(self):
        self.commandQueue.append('down')

    def appendLeft(self):
        self.commandQueue.append('left')

    def appendRight(self):
        self.commandQueue.append('right')

    def change_direction(self):
        if (len(self.commandQueue) > 0):
            command = self.commandQueue.pop(0)
            if command == 'up':
                self.up()
            elif command == 'down':
                self.down()
            elif command == 'left':
                self.left()
            elif command == 'right':
                self.right()

#must be called after snake.go
    def add_head(self):
        self.add_segment(segments[-1].position())

    def up(self):
        if self.head.heading() != DOWN:
            if (self.head.heading() == LEFT or self.head.heading() == RIGHT) \
                    and self.head.ycor() < segments[1].ycor():
                self.head.forward(BLOCK_SIZE)
                self.head.setheading(UP)
            else:
                self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            if (self.head.heading() == LEFT or self.head.heading() == RIGHT) \
                    and self.head.ycor() > segments[1].ycor():
                self.head.forward(BLOCK_SIZE)
                self.head.setheading(DOWN)
            else:
                self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            if (self.head.heading() == UP or self.head.heading() == DOWN) \
                    and self.head.xcor() < segments[1].xcor():
                self.head.forward(BLOCK_SIZE)
                self.head.setheading(RIGHT)
            else:
                self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            if (self.head.heading() == UP or self.head.heading() == DOWN) \
                    and self.head.xcor() > segments[1].xcor():
                self.head.forward(BLOCK_SIZE)
                self.head.setheading(LEFT)
            else:
                self.head.setheading(LEFT)

    def drawBorder(self, screen):
        border = Turtle()
        border.hideturtle()
        border.penup()
        border.color("white")
        border.goto(SCREEN_WIDTH/-2, SCREEN_HEIGHT/-2)
        border.pen(pencolor="gray", pensize=BLOCK_SIZE)
        border.pendown()
        border.goto(SCREEN_WIDTH/2, SCREEN_HEIGHT/-2)
        border.goto(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        border.goto(SCREEN_WIDTH/-2, SCREEN_HEIGHT/2)
        border.goto(SCREEN_WIDTH/-2, SCREEN_HEIGHT/-2)
        screen.update()

    