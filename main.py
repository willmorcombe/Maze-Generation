import pygame
from cell import Cell
import random as r

def main ():

    run = True
    width = 1000
    height = 1000
    win = pygame.display.set_mode((width,height))
    pygame.display.set_caption("Maze Generation")
    clock = pygame.time.Clock()
    win.fill((30, 30, 30))
    grid = initCells(win, width, height)
    stack = []


    current = grid[38]

    while run:

        print(len(stack), len(grid))
        # clock.tick(60)
        current.visited = True
        for cell in grid:
            Cell.show(cell)

        current.highlight()
        neighIndexs = current.getNeighIndex()
        nextPos = notVisitedNeighs(neighIndexs, grid)
        if nextPos is not -1:
            nextPos.visited = True
            stack.append(current)
            removeWalls(current, nextPos)
            current = nextPos

        elif stack != []:
            # print(stack.pop().xIndex)
            current = stack.pop()



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                quit()
                pygame.quit()

        pygame.display.update()




def initCells(win, width, height):
    grid = []
    cellSize = 10
    cols, rows = (int((width - 50) / cellSize), int((height - 50) / cellSize))

    for x in range(rows):
        for y in range(cols):
            grid.append(Cell(win, y, x, cellSize, (cols, rows)))

    return grid


def notVisitedNeighs(l, grid):
    possibleMoves = []

    for index in l:
        if index == -1:
            del(index)
        try:
            if grid[index].visited is False:
                possibleMoves.append(grid[index])
        except:
            continue

    try:
        return r.choice(possibleMoves)
    except:
        return -1

def removeWalls(current, nextPos):
    xVal = current.xIndex - nextPos.xIndex

    if xVal == 1:
        current.edges[1] = False
        nextPos.edges[3] = False
    elif xVal == -1:
        current.edges[3] = False
        nextPos.edges[1] = False

    yVal = current.yIndex - nextPos.yIndex

    if yVal == 1:
        current.edges[0] = False
        nextPos.edges[2] = False
    elif yVal == -1:
        current.edges[2] = False
        nextPos.edges[0] = False








main()

# for index in l:
#     try:
#         if grid[index].visited is False:
#             possibleMoves.append(grid[index])
