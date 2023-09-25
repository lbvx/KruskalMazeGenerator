from __future__ import annotations
import random
from UFDS import UFDS
from pathlib import Path
from PIL import Image

class Maze:
    directions = {
        'N': (-1, 0),
        'S': (1 ,0),
        'E': (0, 1),
        'W': (0, -1)
    }
    rev_directions = {
        'N': 'S',
        'S': 'N',
        'E': 'W',
        'W': 'E'
    }
    
    def __init__(self, rows:int, columns:int, generate=True, seed:int=None) -> None:
        self.rows = rows
        self.columns = columns
        self.solution = None
        self.start = None
        self.end = None

        if generate:
            self.cells = [[{'N': True, 'S': True, 'E': True, 'W': True} for j in range(columns)] for i in range(rows)]  # Mapa do labirinto (inicialmente todas direções fechadas)
            self.__generate_walls()

            random.seed(seed)
            random.shuffle(self.walls)
            self.start = random.randint(0, columns)
            self.end = random.randint(0, columns)
            self.__kruskal()
        else:
            self.cells = [[{'N': False, 'S': False, 'E': False, 'W': False} for j in range(columns)] for i in range(rows)]

    # Cria um Maze a partir de uma imagem gerada pelo algoritmo
    def from_image(image_path:Path) -> Maze:
        image = Image.open(image_path)

        width, height = image.size
        rows = (height - 1) // 2
        columns = (width - 1) // 2

        maze = Maze(rows, columns, generate=False)

        for x in range(width):
            if image.getpixel((x, 0)) == 255:
                maze.start = (x - 1) // 2
            if image.getpixel((x, height - 1)) == 255:
                maze.end = (x - 1) // 2
        
        for y in range(1, height, 2):
            for x in range(1, width, 2):
                x_maze = (x - 1) // 2 
                y_maze = (y - 1) // 2
                if image.getpixel((x, y - 1)) == 0:
                    maze.cells[y_maze][x_maze]['N'] = True
                if image.getpixel((x, y + 1)) == 0:
                    maze.cells[y_maze][x_maze]['S'] = True
                if image.getpixel((x - 1, y)) == 0:
                    maze.cells[y_maze][x_maze]['W'] = True
                if image.getpixel((x + 1, y)) == 0:
                    maze.cells[y_maze][x_maze]['E'] = True

        return maze

    # Cria as possiveis arestas entre vertices
    def __generate_walls(self) -> None:
        self.walls = []
        for i in range(self.rows):
            for j in range(self.columns):
                if i > 0:
                    self.walls.append((i, j, 'N'))
                if i < self.rows - 1:
                    self.walls.append((i, j, 'S'))
                if j > 0:
                    self.walls.append((i, j, 'W'))
                if j < self.columns - 1:
                    self.walls.append((i, j, 'E'))

    # Remove as paredes de forma que o labirinto não tenha partes isoladas, mas sem criar ciclos
    def __kruskal(self) -> None:
        ufds = UFDS(self.rows, self.columns)
        for wall in self.walls:
            cell1 = (wall[0], wall[1])
            dir1 = wall[2]

            cell2 = tuple([sum(x) for x in zip(cell1, Maze.directions[dir1])])
            dir2 = Maze.rev_directions[dir1]

            if ufds.same_set(cell1, cell2):
                continue

            ufds.union(cell1, cell2)
            self.cells[cell1[0]][cell1[1]][dir1] = False
            self.cells[cell2[0]][cell2[1]][dir2] = False

    def __str__(self) -> str:
        s = ''
        for i in range(self.rows):
            for j in range(self.columns):
                if self.cells[i][j]['N']:
                    s += '+--'
                else:
                    s += '+  '
            s += '+\n'
            for j in range(self.columns):
                if self.cells[i][j]['W']:
                    s += '|  '
                else:
                    s += '   '
            if self.cells[i][-1]['E']:        
                s += '|\n'
            else:
                s += ' \n'
        for nj, j in enumerate(self.cells[-1]):
            if nj != self.end:
                s += '+--'
            else:
                s += '+  '
        s += '+\n'

        return s
