from Maze import Maze
from MazeImage import maze_to_image

def main():
    rows = int(input('linhas: '))
    columns = int(input('colunas: '))
    seed = input('semente de aleatoriedade (deixe em branco para aleatório): ')
    if seed == '':
        seed = None
    else:
        seed = int(seed)

    m = Maze(rows, columns, seed=seed)
    
    mi = maze_to_image(m)
    mi.save('maze.png', 'png')

if __name__ == '__main__':
    main()
