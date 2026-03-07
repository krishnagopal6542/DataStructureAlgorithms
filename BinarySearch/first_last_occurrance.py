def get_first_occurrence(array, target):
    left_index = 0
    right_index = len(array) - 1
    mid_index = 0

    target_position = -1

    while left_index <= right_index:
        mid_index = left_index + (right_index - left_index) // 2
        mid_element = array[mid_index]

        if mid_element == target:
            target_position = mid_index
            right_index = mid_index - 1
        elif mid_element > target:
            right_index = mid_index - 1
        else:
            left_index = mid_index + 1
    return target_position

def get_last_occurrence(array, target):
    left_index = 0
    right_index = len(array) - 1
    mid_index = 0
    target_position = -1

    while left_index <= right_index:
        mid_index = left_index + (right_index - left_index) // 2
        mid_element = array[mid_index]

        if target == mid_element:
            target_position = mid_index
            left_index = mid_index + 1
        elif mid_element < target:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1
    return target_position

def get_occurrence(array, target):
    first_occurrence = get_first_occurrence(array, target)
    last_occurrence = get_last_occurrence(array, target)
    return [first_occurrence, last_occurrence]


if __name__ == '__main__':
    num_list = [2, 4, 10, 10, 10, 18, 20]
    num = 10
    res = get_occurrence(num_list, num)
    print(res[1] - res[0] + 1)
