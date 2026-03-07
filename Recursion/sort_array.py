# Sort using recursion

def arr_insert(arr, b):
    if len(arr) == 0 or b >= arr[len(arr) - 1]:
        arr.append(b)
        return

    temp = arr.pop()
    arr_insert(arr, b)
    arr.append(temp)


def array_sort(arr):
    if len(arr) <= 1:
        return

    b = arr.pop()
    array_sort(arr)
    arr_insert(arr, b)


if __name__ == '__main__':
    num = [11, 9, 29, 7, 2, 15, 28]
    array_sort(num)
    print(num)
