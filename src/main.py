from Maze import Maze

def main():
    rows = int(input('linhas: '))
    columns = int(input('colunas: '))
    m = Maze(rows, columns)
    print(str(m))

if __name__ == '__main__':
    main()
