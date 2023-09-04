#!/usr/bin/python3


def is_safe(position, N):
    """
    Checks if a queeen is safe from being killed by another

    Return:
    False if not safe and True if safe

    Args:
    Position: array that contains the position of the queen
    N: Queen number
    """

    for i in range(N):
        if position[i] == position[N]:
            return False
        if abs(position[i] - position[N]) == abs(i - N):
            return False
    return True


def print_position(position, N):
    """Prints the position of queens """

    result = []
    for i in range(N):
        result.append([i, position[i]])
    print(result)


def backtrack_algorithm(position, N):
    """ A function to execute backtracking algorithm """

    if N is len(position):
        print_position(position, N)
        return
    position[N] = -1
    while((position[N] < len(position) - 1)):
        position[N] += 1
        if is_safe(position, N) is True:
            if N is not len(position):
                backtrack_algorithm(position, N + 1)


def solve_N_queen(size):
    """ solve the backtracking algorithm """

    position = [-1 for i in range(size)]
    backtrack_algorithm(position, 0)


if __name__ == '__main__':

    import sys

    if len(sys.argv) == 1 or len(sys.argv) > 2:
        print("USAGE: nqueens N")
        sys.exit(1)
    try:
        size = int(sys.argv[1])
    except Exception:
        print("N must be a number")
        sys.exit(1)

    if size < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_N_queen(size)
