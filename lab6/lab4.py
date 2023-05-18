import numpy as np


def product(arr):
    prod = 1

    for i, item in enumerate(arr):
        if (i % 2 == 0):
            prod *= item

    return prod


def sum(arr):
    sum = 0
    local_sum = 0
    first_zero_item_idx = -1
    last_zero_item_idx = -1

    for i, item in enumerate(arr):
        if (item < 0):
            break

        if (item == 0):
            if (first_zero_item_idx < 0):
                first_zero_item_idx = i

            else:
                last_zero_item_idx = i
                sum += local_sum
                local_sum = 0

            continue

        if (first_zero_item_idx >= 0):
            local_sum += item

    return sum


def custom_sort(arr):
    new_arr = np.array([])
    for item in arr:
        if item >= 0:
            new_arr = np.insert(new_arr, 0, item)
            continue
        new_arr = np.append(new_arr, item)

    return new_arr


arr = []

with open("lab4.txt", "r") as f:
    for line in f.readlines():
        for value in line.split(' '):
            arr.append(int(value))

print('array: {0}'.format(arr))
print('product of positive elements = {0}'.format(product(arr)))

arr = custom_sort(arr)

print('after sort array: {0}'.format(arr))

print(
    'sum of elements between first and last zero elements = {0}'.format(sum(arr)))
