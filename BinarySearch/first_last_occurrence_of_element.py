def get_first_occurrence(array, target):
    start, end = 0, len(array)
    mid = 0
    res = -1
    while start <= end:
        mid_index = start + (end - start) // 2
        mid_element = array[mid_index]

        if target == mid_element:
            res = mid_index
            end = mid_index - 1
        elif target < mid_element:
            end = mid_index - 1
        elif target > mid_element:
            start = mid_index + 1

    return res


def get_last_occurrence(array, target):
    start, end = 0, len(array)
    mid = 0
    res = -1
    while start <= end:
        mid_index = start + (end - start) // 2
        mid_element = array[mid_index]

        if target == mid_element:
            res = mid_index
            start = mid_index + 1
        elif target < mid_element:
            end = mid_index - 1
        elif target > mid_element:
            start = mid_index + 1

    return res


def driver(array, target):
    first_occurrence = get_first_occurrence(array, target)
    last_occurrence = get_last_occurrence(array, target)
    return [first_occurrence, last_occurrence]


if __name__ == '__main__':
    num_list = [5, 7, 7, 8, 8, 10]
    tgt = 8
    print(driver(num_list, tgt))
