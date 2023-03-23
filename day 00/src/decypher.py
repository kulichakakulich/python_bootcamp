import sys


def main():
    if len(sys.argv) == 2:
        result = decypher(sys.argv[1])
        print(result)
    else:
        print('Invalid number of arguments. Usage: python decypher.py "decoding_text"')
        sys.exit(1)


def decypher(strange_text: str):
    return "".join([l[:1] for l in strange_text.split()])


if __name__ == '__main__':
    main()
