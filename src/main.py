from Maze import Maze
from MazeImage import maze_to_image

def main():
    rows = int(input('linhas: '))
    columns = int(input('colunas: '))
    m = Maze(rows, columns)
    
    mi = maze_to_image(m)
    mi.save('maze.png', 'png')

if __name__ == '__main__':
    main()
