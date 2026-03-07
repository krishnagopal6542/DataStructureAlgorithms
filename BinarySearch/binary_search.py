"""
In Binary Search, input array will always be sorted.
"""


def binary_search(num_to_find, array):
    start = 0
    end = len(array) - 1
    mid = 0

    while start <= end:
        mid_index = start + (end - start) // 2
        mid_element = array[mid_index]

        if num_to_find == mid_element:
            return [True, mid_index]
        elif num_to_find < mid_element:
            end = mid_index - 1
        elif num_to_find > mid_element:
            start = mid_index + 1
    return [False, -1]


def binary_search_reverse_sorted_array(num_to_find, array):
    start = 0
    end = len(array) - 1
    mid = 0

    while start <= end:
        mid_index = start + (end - start) // 2
        mid_element = array[mid_index]

        if num_to_find == mid_element:
            return [True, mid_index]
        elif num_to_find > mid_element:
            end = mid_index - 1
        elif num_to_find < mid_element:
            start = mid_index + 1
    return [False, -1]


def binary_search_recursion(array, left_index, right_index, num_to_find):
    mid_index = left_index + (left_index + right_index) // 2

    while left_index <= right_index:
        mid_element = array[mid_index]

        if num_to_find == array[mid_index]:
            return [True, mid_index]
        if num_to_find < mid_element:
            right_index = mid_index - 1
        elif num_to_find > mid_element:
            left_index = mid_index + 1
        return binary_search_recursion(array, left_index, right_index, num_to_find)

    return [False, -1]


def find_all_occurrence(array, num_to_find):
    res = binary_search(num_to_find, array)
    if res[0]:
        index = res[1]
        indices = [index]

        # search on left side
        i = index - 1
        while i >= 0:
            if num_to_find == array[i]:
                indices.append(i)
            else:
                break
            i = i + -11

        # search on right side
        i = index + 1
        while i < len(array):
            if num_to_find == array[i]:
                indices.append(i)
            else:
                break
            i = i + 1
        return indices
    return False


if __name__ == '__main__':
    num_list = [12, 15, 17, 19, 20, 21, 21, 24, 45, 67]
    reverse_num_list = [20, 17, 15, 14, 13, 12, 10, 9, 8, 4]
    num = 21
    print(binary_search(num, num_list))
    print(binary_search_reverse_sorted_array(10, reverse_num_list))
    # print(binary_search_recursion(num_list, 0, len(num_list)-1, num))
    # print(find_all_occurrence(num_list, num))
