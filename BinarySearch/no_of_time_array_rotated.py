def number_of_time_array_is_rotated(array):
    size = len(array)
    left_index = 0
    right_index = size - 1

    while left_index <= right_index:
        mid_index = left_index + (right_index - left_index) // 2
        mid_element = array[mid_index]

        mid_next = (mid_index + 1) % size
        mid_prev = (mid_index + size - 1) % size

        if mid_element <= array[mid_prev] and array[mid_index] <= array[mid_next]:
            return mid_index
        if array[left_index] <= mid_element <= array[right_index]:
            return left_index
        if mid_element <= array[right_index]:
            right_index = mid_index - 1
        if array[left_index] <= mid_element:
            left_index = mid_index + 1

    return -1  # Should never reach here if input is a rotated sorted array


def min_in_rotated_sorted_array(array):
    start, end = 0, len(array) - 1

    while start <= end:
        mid = start + (end - start) // 2

        if array[start] == array[mid] == array[end]:
            start += 1
            end -= 1
        elif array[mid] > array[end]:
            start = mid + 1
        else:
            end = mid

    print(start)
    return array[start]


def debug_min_in_rotated_sorted_array(array):
    start, end = 0, len(array) - 1

    while start < end:
        mid = start + (end - start) // 2
        if array[start] == array[mid] == array[end]:
            start += 1
            end -= 1
        elif array[mid] > array[end]:
            start = mid + 1
        else:
            end = mid

    return array[start]


if __name__ == '__main__':

    # debug_min_in_rotated_sorted_array( [3, 3, 3, 1])
    test_cases = [
        [3, 3, 3, 1],
        [3, 3, 1, 3],  # mid , left , right are equal
        [1, 3, 5],  # No rotation
        [2, 2, 2, 0, 1],  # With duplicates
        [3, 1, 3],  # Simple rotation
        [1, 1, 1, 1]  # All same elements
    ]
    for test in test_cases:
        print(f"Minimum in {test} is: {debug_min_in_rotated_sorted_array(test)}")
