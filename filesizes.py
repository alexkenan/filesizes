"""
Prints list of largest files in a directory
"""
import os
from sys import argv


def prefix(number: Union[int, float]) -> tuple:
    """
    Returns tuple of what to divide by and SI prefix
    :param number: int or float
    :return: tuple of what magnitude to divide number by, and an SI prefix (e.g. (3, 'k') or (9, 'G')
    """
    if isinstance(number, int) or isinstance(number, float):
        _value = {-24: 'y',
                  -21: 'z',
                  -18: 'a',
                  -15: 'f',
                  -12: 'p',
                  -9: 'n',
                  -6: 'u',
                  -3: 'm',
                  -2: 'c',
                  -1: 'd',
                  0: '',
                  3: 'k',
                  6: 'M',
                  9: 'G',
                  12: 'T',
                  15: 'P',
                  18: 'E',
                  21: 'Z',
                  24: 'Y',
                  }
        for i in [-24, -21, -18, -15, -12, -9, -6, -3, -2, -1, 0, 3, 6, 9, 12, 15, 18, 21, 24]:
            if 1 <= number / (1 * 10 ** i) < 1000:
                return i, _value[i]
    else:
        return None


def listsizes(direct: str) -> None:
    """
    Main program:
        List sizes of all files in a directory
    :param direct: A valid path
    :return: None
    """
    if os.path.exists(direct):
        print('')
        sizes = {}
        for file in os.listdir(direct):
            if not file.startswith('.'):
                sizes[file] = os.path.getsize(os.path.join(direct, file))

        for w in sorted(sizes, key=sizes.get, reverse=True):
            i, pref = prefix(sizes[w])

            print('{}: {} {}B'.format(w, round(sizes[w] / 10**i, 2), pref))


if __name__ == '__main__':
    try:
        listsizes(argv[1])
    except IndexError:
        listsizes(input('Input a directory: '))
