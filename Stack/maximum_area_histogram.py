# Leet code: 84
"""
For this, we need to first find the index of nearest smaller to left (NSL) and nearest greater to right(NSR)
once we get NSL & NSR, we can get width by :
    width[i] = NSR[i] - NSi[i] - 1
    rectangle_area[i] = width[i] * array[i]

    max_width = max(rectangle_area]
"""


def nearest_smaller_left(array):
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


def nearest_smaller_right(array):
    n = len(array) - 1
    stack = []
    solution = []
    pseudo_index = len(array)

    while n >= 0:
        if len(stack) == 0:
            solution.append(pseudo_index)
        elif len(stack) > 0 and stack[-1][0] < array[n]:
            solution.append(stack[-1][1])
        elif len(stack) > 0 and stack[-1][0] >= array[n]:
            while len(stack) > 0 and stack[-1][0] > array[n]:
                stack.pop()
            if len(stack) == 0:
                solution.append(pseudo_index)
            else:
                solution.append(stack[-1][1])
        stack.append([array[n], n])
        n -= 1
    solution.reverse()
    return solution


def max_area_histogram(array):
    nsl = nearest_smaller_left(array)
    nsr = nearest_smaller_right(array)

    print("nsl ==> ", nsl)
    print("nsr == >", nsr)

    width = []
    area = []
    max_area = 0
    for i in range(len(array)):
        width.append(nsr[i] - nsl[i] - 1)
        area.append(array[i] * width[i])
        if area[i] > max_area:
            max_area = area[i]

    return max_area


if __name__ == '__main__':
    num = [2, 1, 5, 6, 2, 3]
    print(max_area_histogram(num))
