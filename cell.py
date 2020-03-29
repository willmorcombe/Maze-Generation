import pygame

class Cell:

    def __init__(self, win, x, y, cellSize, dim):
        self.win = win
        self.x = x * cellSize + 25
        self.y = y * cellSize + 25
        self.xIndex = x
        self.yIndex = y
        self.cellSize = cellSize
        self.cols = dim[0]
        self.rows = dim[1]
        left = True
        top =  True
        right = True
        bottom = True
        self.edges = [top, left, bottom, right]
        self.visited = False

    def show(self):

        if self.visited:
            pygame.draw.rect(self.win, (255, 0, 255), (self.x, self.y, self.cellSize, self.cellSize))

        if self.edges[0]:
            pygame.draw.line(self.win, (255, 255, 255), [self.x, self.y], [(self.x + self.cellSize), self.y], 1)
        if self.edges[1]:
            pygame.draw.line(self.win, (255, 255, 255), [self.x, self.y], [self.x, (self.y + self.cellSize)], 1)
        if self.edges[2]:
            pygame.draw.line(self.win, (255, 255, 255), [self.x, (self.y + self.cellSize)], [(self.x + self.cellSize), (self.y + self.cellSize)], 1)
        if self.edges[3]:
            pygame.draw.line(self.win, (255, 255, 255), [(self.x + self.cellSize), (self.y + self.cellSize)],  [(self.x + self.cellSize), self.y], 1)


    def highlight(self):
        pygame.draw.rect(self.win, (255, 0, 0), (self.x, self.y, self.cellSize, self.cellSize))

    def getNeighIndex(self):
        neighs = []
        top = self.getIndex(self.xIndex, self.yIndex -1)
        left = self.getIndex(self.xIndex -1, self.yIndex)
        bottom = self.getIndex(self.xIndex, self.yIndex +1)
        right = self.getIndex(self.xIndex +1, self.yIndex)

        return [top, left, bottom, right]

    def getIndex(self, x, y):
        if x < 0 or x > self.cols -1 or y < 0 or y > self.rows -1:
            return -1
        else:
            return x + y * self.cols




