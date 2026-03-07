# Leet code: 240

def search_in_matrix(matrix, target):
    i, j = 0, len(matrix[0]) - 1
    n, m = len(matrix), len(matrix[0])

    while 0 <= i < n and 0 <= j < m:
        if matrix[i][j] == target:
            return True
        elif matrix[i][j] > target:
            j -= 1
        elif matrix[i][j] < target:
            i += 1
    return False


if __name__ == '__main__':
    _array = [[-1, 3]]
    tgt = 3
    print(search_in_matrix(_array, tgt))
