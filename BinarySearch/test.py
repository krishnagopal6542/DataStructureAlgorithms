def first_occurrence(array, target):
    start, end = 0, len(array) - 1
    _first = -1

    while start <= end:
        mid = start + (end - start) // 2

        if array[mid] == target:
            _first = mid
            end = mid - 1
        elif array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return _first


if __name__ == '__main__':
    num_list = [2, 4, 10, 10, 10, 18, 20]
    key = 10
    print(first_occurrence(num_list, key))
