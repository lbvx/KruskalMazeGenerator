# Kruskal Maze Generator

**Conteúdo da Disciplina**: Grafos 2<br>

## Alunos
| Matrícula | Aluno |
| -- | -- |
| 19/0014032  | Guilherme Rogelin Vial |
| 19/0033088  | Lucas Braun Vieira Xavier |

## [Vídeo](https://youtu.be/1y3XIYs6dXs)

## Sobre

Esse programa utiliza o algoritmo de Kruskal para gerar labirintos, criando aleatoriamente caminhos entre as células (inicialmente todas trancadas), até que haja um caminho de uma célula para qualquer outra, sem haver ciclos.

## Screenshots

![print1](img/20x20.png)

![print2](img/30x50.png)

![print3](img/100x200.png)

## Instalação e execução

Com Python 3 instalado na máquina, primeiro faça no terminal:
```
pip install -r requirements.txt
```
E depois, basta rodar a main.py:
```
python3 src/main.py
```
E seguir as instruções durante a execução. Ao terminar de executar, o programa criará o arquivo de imagem *maze.png* dentro do diretório usado para execução.
