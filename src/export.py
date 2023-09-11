print("Choose an output format:\n1.\tdisplay result in terminal\n2.\texport result as a text file")
choice = int(input(": "))

def output_format(output):
    """
    determines the output format:
    1.  display in terminal
    2.  export as text format
    3.  export as pdf
    4.  ...
    """
    if choice == 1:
        terminal_report(output)
    elif choice == 2:
        text_export(output)

def terminal_report(result):
    print(result)
    print("Welcome to 2D maze")

def text_export(result):
    """
    exports the maze to a text file in the same directory.
    :return: a text file.
    """
    with open("2DMaze.txt", "w") as file:
        file.write(result)
    print('successfully wrote the file in .txt format')
