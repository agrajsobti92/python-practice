matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]

rows = len(matrix)
col = len(matrix[0])
length = rows * col


def binsearch(matrix, target):
    rows = len(matrix)
    col = len(matrix[0])
    length = rows * col

    left = 0
    right = length - 1

    while left <= right:
        mid = int((left + right) / 2)
        r = int(mid / col)
        c = int(mid % col)

        if target > matrix[r][c]:
            left = mid + 1
        elif target < matrix[r][c]:
            right = mid - 1
        else:
            return r, c

    return -1


print(binsearch(matrix, 23))
