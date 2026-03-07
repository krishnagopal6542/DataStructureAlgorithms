def next_smaller_left(array):
    i, n = 0, len(array) - 1
    solution = []
    stack = []

    while i <= n:
        if len(stack) == 0:
            solution.append(-1)
        elif len(stack) > 0 and stack[-1][0] < array[i]:
            solution.append(stack[-1][1])
        elif len(stack) > 0 and stack[-1][0] >= array[i]:
            while len(stack) > 0 and stack[-1][0] >= array[i]:
                stack.pop()
            if len(stack) == 0:
                solution.append(-1)
            else:
                solution.append(stack[-1][1])
        stack.append([array[i], i])
        i += 1

    return solution


def next_smaller_right(array):
    n = len(array) - 1
    stack = []
    solution = []
    pseudo_no = len(array)

    while n >= 0:
        if len(stack) == 0:
            solution.append(pseudo_no)
        elif len(stack) > 0 and stack[-1][0] < array[n]:
            solution.append(stack[-1][1])
        elif len(stack) > 0 and stack[-1][0] >= array[n]:
            while len(stack) > 0 and stack[-1][0] >= array[n]:
                stack.pop()
            if len(stack) == 0:
                solution.append(pseudo_no)
            else:
                solution.append(stack[-1][1])
        stack.append([array[n], n])
        n -= 1

    solution.reverse()
    return solution


def max_area_histogram(array):
    nsl = next_smaller_left(array)
    nsr = next_smaller_right(array)

    width = []
    area = []
    max_area = 0
    for i in range(len(array)):
        width.append(nsr[i] - nsl[i] - 1)
        area.append(array[i] * width[i])
        if area[i] > max_area:
            max_area = area[i]
    return max_area


def main(array):
    row = [0] * len(array[0])
    areaMax = 0
    for i in range(len(array)):
        for j in range(len(array[i])):
            if int(array[i][j]) == 0:
                row[j] = 0
            row[j] = row[j] + int(array[i][j])
        areaMax = max(areaMax, max_area_histogram(row))
    return areaMax


if __name__ == '__main__':
    matrix = [["1", "0", "1", "0", "0"],
              ["1", "0", "1", "1", "1"],
              ["1", "1", "1", "1", "1"],
              ["1", "0", "0", "1", "0"]]
    print(main(matrix))
