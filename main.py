from textToSvg import textToSvg
from textToGcode import svgToGcode


def print_hi():
    textToSvg(['Nice one doods','cool man'],15)
    svgToGcode()


if __name__ == '__main__':
    print_hi()