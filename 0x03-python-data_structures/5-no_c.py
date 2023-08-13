#!/usr/bin/python3
def no_c(my_string):
    length = len(my_string)
    i = 0
    new_string = my_string[:]

    for j in range(length):
        if (my_string[j] == 'c' or my_string[j] == 'C'):
            new_string = new_string[:(j - i)] + new_string[j + 1:]
            i += 1
    return (new_string)
