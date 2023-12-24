def print_grid():
    for row in range(9):
        for col in range(9):
            print(grid[row][col], end=' ')
        print()


def find_empty_square(rc):
    for row in range(9):
        for col in range(9):
            if (grid[row][col] == 0):
                rc[0] = row
                rc[1] = col
                return True
    return False


def used_in_row(row, number):
    for col in range(9):
        if grid[row][col] == number:
            return True
    return False


def used_in_col(col, number):
    for row in range(9):
        if grid[row][col] == number:
            return True
    return False


def used_in_box(row, col, number):
    for x in range(3):
        for y in range(3):
            if grid[x + row][y + col] == number:
                return True
    return False


def verify_safe_square(row, col, number):
    return (not used_in_row(row, number) and
            (not used_in_col(col, number) and
             (not used_in_box(row - row % 3, col - col % 3, number))))


def solve():
    rc = [0, 0]
    if not find_empty_square(rc):
        return True

    row = rc[0]
    col = rc[1]

    for number in range(1, 10):
        if verify_safe_square(row, col, number):

            grid[row][col] = number

            if solve():
                return True

            grid[row][col] = 0
    return False


if __name__ == '__main__':
    grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
            [5, 2, 0, 0, 0, 0, 0, 0, 0],
            [0, 8, 7, 0, 0, 0, 0, 3, 1],
            [0, 0, 3, 0, 1, 0, 0, 8, 0],
            [9, 0, 0, 8, 6, 3, 0, 0, 5],
            [0, 5, 0, 0, 9, 0, 6, 0, 0],
            [1, 3, 0, 0, 0, 0, 2, 5, 0],
            [0, 0, 0, 0, 0, 0, 0, 7, 4],
            [0, 0, 5, 2, 0, 6, 3, 0, 0]]

    if solve():
        print_grid()
    else:
        print("No solution!")
