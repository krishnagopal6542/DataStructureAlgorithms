def next_smaller_to_left(array):
    i, n = 0, len(array) - 1
    solution = []
    stack = []
    while i <= n:
        if len(stack) == 0:
            solution.append(-1)
        elif len(stack) > 0 and stack[-1] < array[i]:
            solution.append(stack[-1])
        elif len(stack) > 0 and stack[-1] >= array[i]:
            while len(stack) > 0 and stack[-1] >= array[i]:
                stack.pop()
            if len(stack) == 0:
                solution.append(-1)
            else:
                solution.append(stack[-1])
        stack.append(array[i])
        i += 1
    return solution


if __name__ == '__main__':
    num = [4, 5, 2, 10, 8]
    print(next_smaller_to_left(num))
