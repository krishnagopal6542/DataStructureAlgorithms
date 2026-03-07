def next_greater_element(array):
    res = []
    stack = []
    i = len(array) - 1

    while i >= 0:
        if len(stack) == 0:
            res.append(-1)
        elif len(stack) > 0 and stack[-1] > array[i]:
            res.append(stack[-1])
        elif len(stack) > 0 and stack[-1] <= array[i]:
            while len(stack) > 0 and stack[-1] <= array[i]:
                stack.pop()
            if len(stack) == 0:
                res.append(-1)
            else:
                res.append(stack[-1])
        stack.append(array[i])

        i -= 1
    return res


def next_greater_to_right(array):
    n = len(array) - 1
    solution = []
    stack = []

    while n >= 0:
        if len(stack) == 0:
            solution.append(-1)
        elif len(stack) > 0 and stack[-1] > array[n]:
            solution.append(stack[-1])
        elif len(stack) > 0 and stack[-1] <= array[n]:
            while len(stack) > 0 and stack[-1] <= array[n]:
                stack.pop()

            if len(stack) == 0:
                solution.append(-1)
            elif stack[-1] > array[n]:
                solution.append(stack[-1])
        stack.append(array[n])
        n -= 1
    solution.reverse()
    return solution


if __name__ == '__main__':
    nums = [1, 3, 2, 4]
    num_1 = [1, 3, 0, 0, 1, 2, 4]
    print(next_greater_to_right(nums))
