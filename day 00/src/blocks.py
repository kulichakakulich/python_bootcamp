import sys


def check_blocks(block_lines, num_lines):
    LINE_LENGTH = 32
    PREFIX_LENGTH = 5

    for i, line in enumerate(block_lines):
        line: str = line.strip()
        if (len(line) != LINE_LENGTH or line[:PREFIX_LENGTH] != "0" * PREFIX_LENGTH
                or line[:PREFIX_LENGTH+1] == "0" * (PREFIX_LENGTH+1)):
            continue
        print(line)
        if num_lines >= 1 and i == int(num_lines) - 1:
            break


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if len(sys.argv) != 2:
            print("Invalid number of arguments. Usage: python blocks.py <num_lines>")
            sys.exit(1)
        try:
            num_lines: int = int(sys.argv[1])
        except ValueError:
            print("Invalid argument: please specify a number of lines to process")
            sys.exit(1)
    else:
        num_lines = 0
    check_blocks(sys.stdin, num_lines)
