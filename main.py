from turtle import Turtle, Screen
from point import Point
from snake import Snake
from food import Food
from scoreboard import Scoreboard

restart = True

screen = Screen()
screen.tracer(0)

screen.setup(width=900, height=900)
screen.bgcolor("black")
screen.title("The Greatest Ever Snake Game")

# SCREEN_HEIGHT = 40
# SCREEN_WIDTH = 40
# BLOCK_SIZE = 5
#
# border = Turtle()
# border.hideturtle()
# border.penup()
# border.color("white")
# border.goto(SCREEN_WIDTH/-2, SCREEN_HEIGHT/-2)
# border.pen(pencolor="gray", pensize=BLOCK_SIZE)
# border.pendown()
# border.goto(SCREEN_WIDTH/2, SCREEN_HEIGHT/-2)
# border.goto(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
# border.goto(SCREEN_WIDTH/-2, SCREEN_HEIGHT/2)
# border.goto(SCREEN_WIDTH/-2, SCREEN_HEIGHT/-2)
# screen.update()
#
# row = 0
# grid = [[]]
# adjacencyList = {}
# for y in range(int(SCREEN_HEIGHT / BLOCK_SIZE / 2) + 1, int(-SCREEN_HEIGHT / BLOCK_SIZE / 2), -1):
#     for x in range(int(-SCREEN_WIDTH/BLOCK_SIZE/2) + 1, int(SCREEN_WIDTH/BLOCK_SIZE/2)):
#         # turt = Turtle()
#         # turt.penup()
#         # turt.showturtle()
#         # turt.goto(x*BLOCK_SIZE, y*BLOCK_SIZE)
#         # turt.color("white")
#         point = Point(x*BLOCK_SIZE, y*BLOCK_SIZE)
#         grid[row].append(point)
#         adjacencyList.update({point: []})
#     grid.append([])
#     row += 1
# screen.update()


# for row in range(0, len(grid)):
#     for col in range(0, len(grid[row])):
#         # if on the top
#         if row == 0:
#             # if on the left
#             if col == 0:
#                 adjacencyList[grid[row][col]].append(grid[row + 1][col])
#                 adjacencyList[grid[row][col]].append(grid[row][col + 1])
#             # if on the right
#             elif col == len(grid[row]) - 1:
#                 adjacencyList[grid[row][col]].append(grid[row + 1][col])
#                 adjacencyList[grid[row][col]].append(grid[row][col - 1])
#             # else
#             else:
#                 adjacencyList[grid[row][col]].append(grid[row + 1][col])
#                 adjacencyList[grid[row][col]].append(grid[row][col - 1])
#                 adjacencyList[grid[row][col]].append(grid[row][col + 1])
#         # if on the bottom
#         elif row == len(grid) - 2:
#             # if on left
#             if col == 0:
#                 adjacencyList[grid[row][col]].append(grid[row - 1][col])
#                 adjacencyList[grid[row][col]].append(grid[row][col + 1])
#             # if on right
#             elif col == len(grid[row]) - 1:
#                 adjacencyList[grid[row][col]].append(grid[row - 1][col])
#                 adjacencyList[grid[row][col]].append(grid[row][col - 1])
#             # else
#             else:
#                 adjacencyList[grid[row][col]].append(grid[row - 1][col])
#                 adjacencyList[grid[row][col]].append(grid[row][col + 1])
#                 adjacencyList[grid[row][col]].append(grid[row][col - 1])
#         # if on left
#         elif col == 0:
#             adjacencyList[grid[row][col]].append(grid[row + 1][col])
#             adjacencyList[grid[row][col]].append(grid[row - 1][col])
#             adjacencyList[grid[row][col]].append(grid[row][col + 1])
#         #if on right
#         elif col == len(grid[row]) - 1:
#             adjacencyList[grid[row][col]].append(grid[row - 1][col])
#             adjacencyList[grid[row][col]].append(grid[row + 1][col])
#             adjacencyList[grid[row][col]].append(grid[row][col - 1])
#         else:
#             adjacencyList[grid[row][col]].append(grid[row + 1][col])
#             adjacencyList[grid[row][col]].append(grid[row - 1][col])
#             adjacencyList[grid[row][col]].append(grid[row][col + 1])
#             adjacencyList[grid[row][col]].append(grid[row][col - 1])

# for key in adjacencyList.keys():
#     print(key, end=": ")
#     for adj in adjacencyList[key]:
#         print(adj, end=" ")
#     print("")

# for row in range(0, len(grid)):
#     for col in range(0, len(grid[row])):
#         # if on the top
#         if row == 0:
#             # if on the left
#             if col == 0:
#                 print(grid[col][row], end="")
#             # if on the right
#             elif col == len(grid[row]) - 1:
#                 print(grid[row][col])
#             # else
#             else:
#                 print(grid[row][col], end="")
#         # if on the bottom
#         elif row == len(grid) - 2:
#             # if on left
#             if col == 0:
#                 print(grid[row][col], end="")
#             # if on right
#             elif col == len(grid[row]) - 1:
#                 print(grid[row][col])
#             # else
#             else:
#                 print(grid[row][col], end="")
#         # if on left
#         elif col == 0:
#             print(grid[row][col], end="")
#         # if on right
#         elif col == len(grid[row]) - 1:
#             print(grid[row][col])
#         else:
#             print(grid[row][col], end="")


food = Food()
game_is_on = True
scoreboard = Scoreboard()
snake = Snake(length=5, screen=screen)

while game_is_on:
    snake.go(screen, speed=0.1)
    game_is_on = snake.check_collision(food, scoreboard)

print(snake.head.pos())


screen.exitonclick()
