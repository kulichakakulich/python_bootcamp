import sys

M_POS = [0, 4, 5, 6, 8, 9, 10, 12, 14]


def read_input(filename: str):
    try:
        with open(filename, "r") as f:
            lines = f.read().splitlines()
            if len(lines) != 3 or any(len(row) != 5 for row in lines):
                return None
            return "".join(lines)
    except FileNotFoundError:
        return None


def check_pattern(image: str):
    if (all(image[i] == '*' for i in M_POS) and
            all(image[i] != '*' for i in range(len(image)) if i not in M_POS)):
        return True
    else:
        return False


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python mfinder.py <input_file>")
        sys.exit(1)
    image = read_input(sys.argv[1])
    if image is None:
        print("Error")
        sys.exit(1)
    if check_pattern(image):
        print("True")
    else:
        print("False")
