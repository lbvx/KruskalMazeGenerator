from PIL import Image
from Maze import Maze
from random import randrange

def maze_to_image(maze:Maze) -> Image:
    size = (2 * maze.columns + 1, 2 * maze.rows + 1)
    maze_image = Image.new('1', size)

    for y in range(1, size[1], 2):
        for x in range(1, size[0], 2):
            maze_image.putpixel((x, y), 1)

    for i, row in enumerate(maze.cells):
        for j, cell in enumerate(row):
            y = 2 * i + 1
            x = 2 * j + 1
            if not cell['E']:
                maze_image.putpixel((x + 1, y), 1)
            if not cell['S']:
                maze_image.putpixel((x, y + 1), 1)

    start = maze.start * 2 + 1
    end = maze.end * 2 + 1

    maze_image.putpixel((start, 0), 1)
    maze_image.putpixel((end, size[1] - 1), 1)

    return maze_image
