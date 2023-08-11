#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    length = len(argv) - 1

    if length == 0:
        print("{} arguments.".format(length))
    elif length == 1:
        print("{} argument:".format(length))
    else:
        print("{} arguments:".format(length))
    if length >= 1:
        length = 0
        for arg in argv:
            if length != 0:
                print("{}: {}".format(length, arg))
            length += 1
