import random

class Node():
    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.isWall = False
        self.isOpen = None
        self.f = 0
        self.g = 0
        self.h = 0
        self.neighbors = []
        self.previous = None

    def __repr__(self):
        return f'< i = {self.i}, j = {self.j}, previous = {self.previous} >'

    def add_neighbors(self, grid, diagonal):
        i = self.i
        j = self.j

        if i > 0:
            self.neighbors.append(grid[i - 1][j])

        if i < len(grid) - 1:
            self.neighbors.append(grid[i + 1][j])


        if j > 0:
            self.neighbors.append(grid[i][j - 1])

        if j < len(grid) - 1:
            self.neighbors.append(grid[i][j + 1])

        if diagonal:
            # for diagonal neighbors

            # down and right
            if i < len(grid) - 1 and j < len(grid) - 1:
                self.neighbors.append(grid[i + 1][j + 1])

            # up and right
            if i > 0 and j < len(grid) - 1:
                self.neighbors.append(grid[i - 1][j + 1])

            #down and left
            if i < len(grid) - 1 and j > 0:
                self.neighbors.append(grid[i + 1][j - 1])

            #up and left
            if i > 0 and j > 0:
                self.neighbors.append(grid[i - 1][j - 1])




def make_grid(length, start, end, diag):
    # start and end are lists for the start and end positions

    main_grid = []
    for i in range(length):
        lst = []

        for j in range(length):
            node = Node(i, j)

            # 30 % chance that the current node will be set as a wall
            r = random.randrange(1, 101)

            # if r > 70 and ((i != start[0] and j != start[1]) or (i != end[0] and j!= end[1])): 
            #     node.isWall = True

            if r > 70 and [i, j] != start and [i, j] != end: 
                node.isWall = True

            lst.append(node)

        main_grid.append(lst)


    for i in range(length):
        for j in range(length):
            
            main_grid[i][j].add_neighbors(main_grid, diagonal = diag)
 

    return main_grid




