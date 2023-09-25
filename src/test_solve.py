from Maze import Maze
from MazeSolver import MazeSolver
from pathlib import Path
from sys import argv
import time

def main(argv):
    image_path = Path(argv[1])
    searches = argv[2:]
    if len(searches) == 0:
        searches = ['bfs']

    for s in searches:
        t0_gen = time.time()
        maze = Maze.from_image(image_path)
        solver = MazeSolver(maze, search=s,search_all=False)
        t1_gen = time.time()

        t0_solve = time.time()
        solver.solve()
        t1_solve = time.time()

        t0_img = time.time()
        img = solver.solution_nodes_to_image()
        img.save(f'teste/solution_{s}.png', 'png')
        t1_img = time.time()

        print(f'{solver.maze.rows}x{solver.maze.columns} - {s}:')
        print(f'\tTempo para carregar labirinto: {(t1_gen - t0_gen):.2f}s')
        print(f'\tTempo para resolver: {(t1_solve - t0_solve):.2f}s')
        print(f'\tTotal de nós explorados: {len(solver.nodes)}')
        print(f'\tTempo para gerar imagem: {(t1_img - t0_img):.2f}s')
        print()

if __name__ == '__main__':
    main(argv)
