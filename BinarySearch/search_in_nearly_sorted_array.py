def binary_search_on_nearly_sorted_array(array, target):
    start, end = 0, len(array) - 1
    size = len(array)
    while start <= end:
        mid = start + (end - start) // 2

        if array[mid] == target:
            return mid
        prev = (mid - 1) % size
        next = (mid + 1) % size

        if array[prev] == target:
            return prev
        elif array[next] == target:
            return next
        elif target < array[mid]:
            end = mid - 2
        elif target > array[mid]:
            start = mid + 2
    return -1


if __name__ == '__main__':
    num = [5, 10, 30, 20, 40]
    tgt = 10
    print(binary_search_on_nearly_sorted_array(num, tgt))
