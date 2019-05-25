"""
    Created by chaupm at 2019-05-22
"""
import numpy as np

SQUARE_SIZE = 3
RUN_OUT_OF_SQUARE_CODE = -1


def check(square):
    for i in range(len(square)):
        row = square[i]
        if len(set(row)) != 3:
            return False

    for i in range(len(square)):
        col = square[:, i]
        if len(set(col)) != 3:
            return False
    return True


def pretty_print(square):
    for row in square:
        for i in row:
            print(i.decode("utf-8"), end=" ")
        print("\n", end="")


def find_next(r, c):
    if c < SQUARE_SIZE - 1:
        return (r, c + 1)
    elif r < SQUARE_SIZE - 1:
        return (r + 1, 0)
    else:
        return (RUN_OUT_OF_SQUARE_CODE, RUN_OUT_OF_SQUARE_CODE)


def generate_helper(square, r, c):
    if r == RUN_OUT_OF_SQUARE_CODE:
        is_true = check(square)
        pretty_print(square)

        if is_true:
            print("true")

        print("----------")
        return check(square)

    square_a = square.copy()
    square_b = square.copy()
    square_c = square.copy()

    square_a[r, c] = "a"
    square_b[r, c] = "b"
    square_c[r, c] = "c"

    r_next, c_next = find_next(r, c)

    return generate_helper(square_a, r_next, c_next) + generate_helper(square_b, r_next, c_next) + generate_helper(
        square_c, r_next, c_next)


def sol():
    square = np.zeros((SQUARE_SIZE, SQUARE_SIZE), dtype='S1')
    r = c = 0
    nums = generate_helper(square, r, c)
    return nums


if __name__ == '__main__':
    print(sol())
