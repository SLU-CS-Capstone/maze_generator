from maze import Maze
import argparse

def get_parsed_args():
    parser = argparse.ArgumentParser(
        prog="maze-generator",
        description="Generate NxN sized mazes",
    )
    parser.add_argument(
        "--output",
        choices=["print", "file"],
        default="print",
        help="Specify type of output",
    )
    parser.add_argument(
        "--size", 
        help="Set size of generated maze",
        type=int,
        required=True
    )

    args = parser.parse_args()
    return args

def main():
    print("Welcome to 2D maze")
    args = get_parsed_args()
    maze = Maze(args.size)
    maze.generate_maze()
    maze.print(to_file=args.output == "file")
    
if __name__ == "__main__":
    main()
