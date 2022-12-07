class Graph:
    def __init__(self, width, height, blockSize):
        self.width = width
        self.height = height
        self.blockSize = blockSize
        self.grid = [[]]
        self.adjacencyList = {}


    def create_grid(self):
        row = 0
        for y in range(int(self.height / self.blockSize / 2) + 1, int(-self.height / self.blockSize / 2), -1):
            for x in range(int(-self.width / self.blockSize / 2) + 1, int(self.width / self.blockSize / 2)):
                # turt = Turtle()
                # turt.penup()
                # turt.showturtle()
                # turt.goto(x*self.blockSize, y*self.blockSize)
                # turt.color("white")
                point = Point(x * self.blockSize, y * self.blockSize)
                self.grid[row].append(point)
                self.adjacencyList.update({point: []})
            self.grid.append([])
            row += 1
        # screen.update()
    
    def make_adjacency_list(self):
        for row in range(0, len(self.grid)):
            for col in range(0, len(self.grid[row])):
                # if on the top
                if row == 0:
                    # if on the left
                    if col == 0:
                        self.adjacencyList[self.grid[row][col]].append(self.grid[row + 1][col])
                        self.adjacencyList[self.grid[row][col]].append(self.grid[row][col + 1])
                    # if on the right
                    elif col == len(self.grid[row]) - 1:
                        self.adjacencyList[self.grid[row][col]].append(self.grid[row + 1][col])
                        self.adjacencyList[self.grid[row][col]].append(self.grid[row][col - 1])
                    # else
                    else:
                        self.adjacencyList[self.grid[row][col]].append(self.grid[row + 1][col])
                        self.adjacencyList[self.grid[row][col]].append(self.grid[row][col - 1])
                        self.adjacencyList[self.grid[row][col]].append(self.grid[row][col + 1])
                # if on the bottom
                elif row == len(self.grid) - 2:
                    # if on left
                    if col == 0:
                        self.adjacencyList[self.grid[row][col]].append(self.grid[row - 1][col])
                        self.adjacencyList[self.grid[row][col]].append(self.grid[row][col + 1])
                    # if on right
                    elif col == len(self.grid[row]) - 1:
                        self.adjacencyList[self.grid[row][col]].append(self.grid[row - 1][col])
                        self.adjacencyList[self.grid[row][col]].append(self.grid[row][col - 1])
                    # else
                    else:
                        self.adjacencyList[self.grid[row][col]].append(self.grid[row - 1][col])
                        self.adjacencyList[self.grid[row][col]].append(self.grid[row][col + 1])
                        self.adjacencyList[self.grid[row][col]].append(self.grid[row][col - 1])
                # if on left
                elif col == 0:
                    self.adjacencyList[self.grid[row][col]].append(self.grid[row + 1][col])
                    self.adjacencyList[self.grid[row][col]].append(self.grid[row - 1][col])
                    self.adjacencyList[self.grid[row][col]].append(self.grid[row][col + 1])
                # if on right
                elif col == len(self.grid[row]) - 1:
                    self.adjacencyList[self.grid[row][col]].append(self.grid[row - 1][col])
                    self.adjacencyList[self.grid[row][col]].append(self.grid[row + 1][col])
                    self.adjacencyList[self.grid[row][col]].append(self.grid[row][col - 1])
                else:
                    self.adjacencyList[self.grid[row][col]].append(self.grid[row + 1][col])
                    self.adjacencyList[self.grid[row][col]].append(self.grid[row - 1][col])
                    self.adjacencyList[self.grid[row][col]].append(self.grid[row][col + 1])
                    self.adjacencyList[self.grid[row][col]].append(self.grid[row][col - 1])