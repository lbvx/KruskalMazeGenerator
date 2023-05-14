import random
from UFDS import UFDS

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
    
    def __init__(self, rows:int, columns:int, seed:int=None) -> None:
        self.rows = rows
        self.columns = columns
        self.cells = [[{'N': True, 'S': True, 'E': True, 'W': True} for j in range(columns)] for i in range(rows)]
        self.__generate_walls()

        random.seed(seed)
        random.shuffle(self.walls)
        self.__kruskal()

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

    def print(self) -> None:
        for i in range(self.rows):
            for j in range(self.columns):
                if self.cells[i][j]['N']:
                    print("+--", end="")
                else:
                    print("+  ", end="")
            print('+')
            for j in range(self.columns):
                if self.cells[i][j]['W']:
                    print("|  ", end="")
                else:
                    print("   ", end="")
            print('|')
        for j in self.cells[-1]:
            print("+--", end='')
        print('+') 
