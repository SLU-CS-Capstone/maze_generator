from maze import Maze
import argparse


def parsing_arguments():
    """
    receives arguments from user to create the maze
    size: is the size of the maze (default 20)
    output_format: is the output format: pdf, txt, terminal (default terminal)
    returns: arguments object with the arguments from user
    """
    parser = argparse.ArgumentParser(description="maze generator")
    parser.add_argument('-o', '--output_format', choices=['pdf', 'txt', 'terminal'], 
                        default='terminal', help='It specifies the output format')
    parser.add_argument('-s', '--size', default=20, type=int, help='It specifies the size of the maze')
    arguments = parser.parse_args()
    return arguments


if __name__ == '__main__':
    print("Welcome to 2D Maze")
    argument = parsing_arguments()
    maze = Maze(argument.size)
    maze.generate_maze()
    maze.print(argument.output_format)
    