def next_smaller_to_right(array):
    n = len(array) - 1
    solution = []
    stack = []
    while n >= 0:
        if len(stack) == 0:
            solution.append(-1)
        elif len(stack) > 0 and stack[-1] < array[n]:
            solution.append(stack[-1])
        elif len(stack) > 0 and stack[-1] >= array[n]:
            while len(stack) > 0 and stack[-1] > array[n]:
                stack.pop()
            if len(stack) == 0:
                solution.append(-1)
            else:
                solution.append(stack[-1])
        stack.append(array[n])
        n -= 1
    solution.reverse()
    return solution


if __name__ == '__main__':
    num = [4, 5, 2, 10, 8]
    print(next_smaller_to_right(num))
