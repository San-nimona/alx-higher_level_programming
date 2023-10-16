#!/usr/bin/python3
""" Doc """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(10, 10, 10, 10)
    try:
        print(r1)
    except Exception as e:
        print('[{}] {}'.format(e.__class__.__name__, e))

    try:
        r1.update(89)
        print(r1)
    except Exception as e:
        print('[{}] {}'.format(e.__class__.__name__, e))

    try:
        r1.update("yes", 2)
        print(r1)
    except Exception as e:
        print('[{}] {}'.format(e.__class__.__name__, e))

    try:
        r1.update(89, 2, -3)
        print(r1)
    except Exception as e:
        print('[{}] {}'.format(e.__class__.__name__, e))

    try:
        r1.update(89, 2, 3, True)
        print(r1)

    except Exception as e:
        print('[{}] {}'.format(e.__class__.__name__, e))

    try:
        r1.update(89, "2", 3, 4, 5)
        print(r1)
    except Exception as e:
        print('[{}] {}'.format(e.__class__.__name__, e))
