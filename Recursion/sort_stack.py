"""
In python, stack can't be implemented directly.
It can be implemented using the following ways:
    *   List
    *   Collections.deque
    *   queue.LifoQueue

We will use list for stack implementation, as list support stack functionality.
"""


def arr_insert(arr, b):
    if len(arr) == 0 or b >= arr[len(arr) - 1]:
        arr.append(b)
        return

    temp = arr.pop()
    arr_insert(arr, b)
    arr.append(temp)


def sort_stack(arr):
    if len(arr) <= 1:
        return

    b = arr.pop()
    sort_stack(arr)
    arr_insert(arr, b)


if __name__ == '__main__':
    num = [11, 9, 29, 7, 2, 15, 28]
    sort_stack(num)
    print(num)
