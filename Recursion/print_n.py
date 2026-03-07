# Print from N to 1 using recursion

def print_n_to_1(n):
    if n == 0:
        return
    print_n_to_1(n - 1)
    print(n)


def print_1_to_n(n):
    if n == 0:
        return
    print(n)
    print_1_to_n(n - 1)


def insertion_sort(elements):
    for i in range(1, len(elements)):
        anchor = elements[i]
        j = i - 1

        while j >= 0 and anchor < elements[j]:
            elements[j + 1] = elements[j]
            j -= 1
        elements[j + 1] = anchor
    print(elements)


def arr_insert(arr, b):
    if len(arr) == 0 or b >= arr[len(arr) - 1]:
        arr.append(b)
        return
    temp = arr.pop()
    arr_insert(arr, b)
    arr.append(temp)


def sort_array_recursion(arr):
    if len(arr) <= 1:
        return

    b = arr.pop()
    sort_array_recursion(arr)
    arr_insert(arr, b)


if __name__ == '__main__':
    # print_n_to_1(10)
    # print_1_to_n(10)
    num = [11, 9, 29, 7, 2, 15, 28]
    # insertion_sort([11, 9, 29, 7, 2, 15, 28])
    sort_array_recursion(num)
    print(num)
