def exporter(result, output_format):
    """
    determines the output format:
    """
    if output_format == 'terminal':
        terminal_report(result)
    elif output_format == 'txt':
        text_export(result)


def terminal_report(result):
    """
    displays the maze in terminal
    """
    print(result)


def text_export(result):
    """
    exports the maze as a text file in the same /src directory.
    """
    with open("2DMaze.txt", "w") as file:
        file.write(result)
    print('successfully wrote the file in 2DMaze.txt file')
    