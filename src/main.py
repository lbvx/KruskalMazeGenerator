from Maze import Maze
from MazeImage import maze_to_image

def menu() -> tuple:
    err = True
    while err:
        try:
            rows = int(input('linhas: '))
            if rows <= 0:
                raise ValueError()
            err = False
        except ValueError:
            print("Somente valores inteiros maiores que 0 para a quantidade de linhas!")
    err = True
    while err:
        try:
            columns = int(input('colunas: '))
            if columns <= 0:
                raise ValueError()
            err = False
        except ValueError:
            print("Somente valores inteiros maiores que 0 para a quantidade de colunas!")
    err = True
    while err:
        try:
            seed = input('semente de aleatoriedade (deixe em branco para aleatório): ')
            if seed == '':
                seed = None
            else:
                seed = int(seed)
            err = False
        except ValueError:
            print("Somente valores numéricos ou nada!")
    return (rows, columns, seed)


def main():
    rows, columns, seed = menu()
    
    m = Maze(rows, columns, seed=seed)
    
    mi = maze_to_image(m)
    mi.save('maze.png', 'png')

if __name__ == '__main__':
    main()
