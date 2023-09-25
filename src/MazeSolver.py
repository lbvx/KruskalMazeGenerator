from Maze import Maze
from collections import deque
from MazeImage import maze_to_image
from PIL import Image

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

class MazeSolver:
    def __init__(self, maze:Maze, search_all=True, use_dfs=False) -> None:
        self.maze = maze
        self.nodes = []
        self.solution = None
        self.search_all = search_all
        self.use_dfs = use_dfs

    def solve(self) -> None:
        if self.maze.start is None or self.maze.end is None:
            raise Exception("Can't solve maze without set start and end")
        
        self.__find_nodes()

        self.solution = []

        node = self.end_node
        while node != self.start_node:
            self.solution.append(node[:3])
            node = node[3]
        
        self.solution.append(self.start_node[:3])

    def __find_nodes(self) -> None:
        self.start_node = (0, self.maze.start, 'N', None)
        self.end_node = None
        self.nodes = [self.start_node]
        queue = deque()
        queue.append(self.nodes[0])
        while len(queue) > 0:
            n = queue.pop() if self.use_dfs else queue.popleft()
            n_y, n_x, n_parent_dir, parent = n
            for direction in directions.keys():
                if direction == n_parent_dir:
                    continue
                next_y, next_x = n_y, n_x
                while not self.maze.cells[next_y][next_x][direction]:
                    next_y += directions[direction][0]
                    next_x += directions[direction][1]
                    if next_y >= self.maze.rows or next_y < 0 or next_x >= self.maze.columns or next_x < 0:
                        break
                    
                    if any([not self.maze.cells[next_y][next_x][d] for d in set(directions.keys()) - set([direction, rev_directions[direction]])]):
                        new_node = (next_y, next_x, rev_directions[direction], n)
                        if new_node[0:2] == (self.maze.rows - 1, self.maze.end):
                            self.end_node = new_node
                            if not self.search_all:
                                return
                            
                        self.nodes.append(new_node)
                        queue.append(new_node)
                        break
        
    def nodes_to_image(self):
        NODES_COLOR = (0, 230, 90)

        nodes_image = maze_to_image(self.maze).convert('RGB')

        for node in self.nodes:
            im_y = node[0] * 2 + 1
            im_x = node[1] * 2 + 1

            nodes_image.putpixel((im_x, im_y), NODES_COLOR)

        return nodes_image

    def solution_to_image(self):
        PATH_COLOR = (200, 0, 90)
        solution_image = maze_to_image(self.maze).convert('RGB')

        im_start = self.maze.start * 2 + 1
        im_end = self.maze.end * 2 + 1
        solution_image.putpixel((im_start, 0), PATH_COLOR)
        solution_image.putpixel((im_end, self.maze.rows * 2), PATH_COLOR)

        for i, node in enumerate(self.solution[:-1]):
        # for node in self.solution:
            im_y = node[0] * 2 + 1
            im_x = node[1] * 2 + 1
            solution_image.putpixel((im_x, im_y), PATH_COLOR)

            next_node = self.solution[i + 1]

            while (im_y, im_x) != (next_node[0] * 2 + 1, next_node[1] * 2 + 1):
                im_y += directions[node[2]][0]
                im_x += directions[node[2]][1]
                solution_image.putpixel((im_x, im_y), PATH_COLOR)

        return solution_image
    
    def solution_nodes_to_image(self):
        NODES_COLOR = (0, 230, 90)
        PATH_COLOR = (200, 0, 90)

        solution_image = maze_to_image(self.maze).convert('RGB')

        for node in self.nodes:
            im_y = node[0] * 2 + 1
            im_x = node[1] * 2 + 1

            solution_image.putpixel((im_x, im_y), NODES_COLOR)

        im_start = self.maze.start * 2 + 1
        im_end = self.maze.end * 2 + 1
        solution_image.putpixel((im_start, 0), PATH_COLOR)
        solution_image.putpixel((im_end, self.maze.rows * 2), PATH_COLOR)

        for i, node in enumerate(self.solution[:-1]):
        # for node in self.solution:
            im_y = node[0] * 2 + 1
            im_x = node[1] * 2 + 1
            solution_image.putpixel((im_x, im_y), PATH_COLOR)

            next_node = self.solution[i + 1]

            while (im_y, im_x) != (next_node[0] * 2 + 1, next_node[1] * 2 + 1):
                im_y += directions[node[2]][0]
                im_x += directions[node[2]][1]
                solution_image.putpixel((im_x, im_y), PATH_COLOR)

        return solution_image