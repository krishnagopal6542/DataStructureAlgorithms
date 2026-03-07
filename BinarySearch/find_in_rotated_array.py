def binary_search(array, target, left_index, right_index):
    while left_index <= right_index:
        mid_index = left_index + (right_index - left_index) // 2
        mid_element = array[mid_index]

        if mid_element == target:
            return mid_index
        elif mid_element < target:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1
    return -1


def get_min_value_index(array):
    start, end = 0, len(array) - 1
    n = len(array)

    while start <= end:
        mid = start + (end - start) // 2
        mid_next = (mid + 1) % n
        mid_prev = (mid + n - 1) % n

        if array[mid] <= array[mid_next] and array[mid] <= array[mid_prev]:
            return mid
        if array[start] <= array[mid] <= array[end]:
            return start
        if array[start] <= array[mid]:
            start = mid + 1
        else:
            end = mid - 1


def search_in_rotated_array(array, target):
    min_val_index = get_min_value_index(array)
    print("min_val_index == >", min_val_index)
    left_search = binary_search(array, target, 0, min_val_index - 1)
    right_search = binary_search(array, target, min_val_index, len(array) - 1)

    return right_search if left_search == -1 else left_search


if __name__ == '__main__':
    num_list = [4, 5, 6, 7, 0, 1, 2]
    num = 1
    print(search_in_rotated_array(num_list, num))
