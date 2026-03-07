def next_greater_to_left(array):
    i, n = 0, len(array) - 1
    solution = []
    stack = []

    while i <= n:
        if len(stack) == 0:
            solution.append(-1)
        elif len(stack) > 0 and stack[-1] > array[i]:
            solution.append(stack[-1])
        elif len(stack) > 0 and stack[-1] <= array[i]:
            while len(stack) > 0 and stack[-1] <= array[i]:
                stack.pop()
            if len(stack) == 0:
                solution.append(-1)
            else:
                solution.append(stack[-1])
        stack.append(array[i])
        i += 1
    return solution

def next_greater_to_left_stock_span(array):
    i, n = 0, len(array) - 1
    solution = []
    stack = []

    while i <= n:
        if len(stack) == 0:
            solution.append(-1)
        elif len(stack) > 0 and stack[-1][0] > array[i]:
            solution.append(stack[-1][1])
        elif len(stack) > 0 and stack[-1][0] <= array[i]:
            while len(stack) > 0 and stack[-1][0] <= array[i]:
                stack.pop()
            if len(stack) == 0:
                solution.append(-1)
            else:
                solution.append(stack[-1][1])
        stack.append([array[i], i])
        i += 1

    for i in range(len(solution)):
        solution[i] = i - solution[i]
    return solution

if __name__ == '__main__':
    num = [100, 80, 60, 70, 60, 75, 85] #,[1, 3, 2, 4]
    print(next_greater_to_left(num))
