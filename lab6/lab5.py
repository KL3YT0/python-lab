import numpy as np


def col_count(matrix):
    count = 0

    M = len(matrix)
    N = len(matrix[0])

    for i in range(N):
        for j in range(M):
            if (matrix[j][i] == 0):
                count += 1
                j = M - 1
                break

    return count


def max_row_series(row):
    curr_item = row[0]
    max_series = 0
    curr_series = 1

    for item in row[1:]:
        if item == curr_item:
            curr_series += 1
            continue

        curr_item = item
        max_series = max([max_series, curr_series])
        curr_series = 1

    return max([max_series, curr_series])


def row_num(matrix):
    row = 0
    max_series = 0
    curr_series = 0

    for i, item in enumerate(matrix):
        curr_series = max_row_series(item)

        if (curr_series > max_series):
            max_series = curr_series
            row = i

    return [row, max_series]


matrix = []

with open("lab5.txt", "r") as f:
    for i, line in enumerate(f.readlines()):
        matrix.append([])
        for value in line.split(' '):
            matrix[i].append(int(value))

matrix = np.array(matrix)

print('matrix: \n', matrix)

print('count of cols with zero element: ', col_count(matrix))

row, max_series = row_num(matrix)

print('row number with the longest series of identical elements: ', row)
print('the longest series of identical elements: ', max_series)
