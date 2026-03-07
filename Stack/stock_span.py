"""
This is similar to the greatest element to the left.
The Only difference is that we need to find the index greatest left element.
So for that, we will store the left greatest element and its index in the stack.
And will compare the stack element along with will store its relevant index in the solution vector.
"""


def stock_span(array):
    i, n = 0, len(array) - 1
    stack = []
    solution = []

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
    num = [1, 3, 2, 4]
    print(stock_span(num))
