from queue import Queue
from point import Point


class Graph:
    def __init__(self, width, height, blockSize):
        self.width = width
        self.height = height
        self.blockSize = blockSize
        self.grid = [[]]
        self.adjacencyList = {}
        self.create_grid()
        self.make_adjacency_list()

    def find_route_bfs(self, start, end):
        previous = {}
        visited = []
        frontier = Queue()

        current = start
        frontier.put(current)
        visited.add(current)
        while not frontier.empty():
            current = frontier.get()
            for neighbor in self.adjacencyList[current]::
                if neighbor not in visited:
                    previous.update(neighbor, current)
                    visited.add(neighbor)
                    frontier.add(neighbor)

        result = []
        result.append(end)
        curr = previous[end]
        while current != start:
            result.add(curr)
            curr = previous[curr]
        result.add(curr)
        result.reverse()
        return result



    def create_grid(self):
        row = 0
        for y in range(int(self.height / self.blockSize / 2) + 1, int(-self.height / self.blockSize / 2), -1):
            for x in range(int(-self.width / self.blockSize / 2) + 1, int(self.width / self.blockSize / 2)):
                point = Point(x * self.blockSize, y * self.blockSize)
                self.grid[row].append(point)
                self.adjacencyList.update({point: []})
            self.grid.append([])
            row += 1
    
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