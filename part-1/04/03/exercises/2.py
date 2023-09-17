correct = [[1, 2, 3],
           [2, 3, 1],
           [3, 1, 2]]

incorrect = [[1, 2, 3, 4],
             [2, 3, 1, 3],
             [3, 1, 2, 3],
             [4, 4, 4, 4]]

incorrect2 = [[1, 2, 3, 4],
              [2, 3, 1, 4],
              [4, 1, 2, 3],
              [3, 4, 1, 2]]

incorrect3 = [[1, 2, 3, 4, 5],
              [2, 3, 1, 5, 6],
              [4, 5, 2, 1, 3],
              [3, 4, 5, 2, 1],
              [5, 6, 4, 3, 2]]

incorrect4 = [['a', 'b', 'c'],
              ['b', 'c', 'a'],
              ['c', 'a', 'b']]

incorrect5 = [[1, 1.5],
              [1.5, 1]]


# Define a function check_sudoku() here:
def check_sudoku(square):
    # in case that number is  out of range
    for row in square:
        for num in row:
            if num not in range(1, len(square) + 1):
                return False

    for i in range(len(square)):
        row = []
        col = []
        for j in range(len(square)):
            row.append(square[i][j])
            col.append(square[j][i])
        if sorted(row) != list(range(1, len(square) + 1)) or sorted(col) != list(range(1, len(square) + 1)):
            return False

    return True


print(check_sudoku(incorrect))

print(check_sudoku(correct))

print(check_sudoku(incorrect2))

print(check_sudoku(incorrect3))

print(check_sudoku(incorrect4))

print(check_sudoku(incorrect5))
