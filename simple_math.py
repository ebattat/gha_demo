# simple_math.py

import sys


def add(a, b):
    """Return the sum of a and b."""
    return a + b


if __name__ == "__main__":
    args = sys.argv
    a = int(args[1]) if len(args) > 1 else 1
    b = int(args[2]) if len(args) > 2 else 3
    print(add(a, b))
