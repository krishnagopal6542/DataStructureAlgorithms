"""
Order Agnostic Search

Write two Branch Search Function
    i. Search in  sorted array
    ii. Search in reverse sorted array

Check nearby position of array and call each function accordingly
"""



def binary_search(array, target):
    start, end = 0, len(array)
    mid = 0

    while start <= end:
        mid_index = start + (end - start) // 2
        mid_element = array[mid_index]

        if mid_element == target:
            return [True, mid_index]
        elif target > mid_element:
            start = mid_index + 1
        elif target < mid_element:
            end = mid_index - 1
    return [False, -1]


def binary_search_reverse_order(array, target):
    start, end = 0, len(array)
    mid = 0

    while start <= end:
        mid_index = start + (end - start) // 2
        mid_element = array[mid_index]

        if target == mid_element:
            return [True, mid_index]
        elif target > mid_element:
            end = mid_index - 1
        elif target < mid_element:
            start = mid_index + 1
    return [False, -1]


def driver(array, target):
    if len(array) and target == array[0]:
        return [True, 0]
    elif array[0] < array[1]:
        return binary_search(array, target)
    else:
        return binary_search_reverse_order(array, target)


if __name__ == '__main__':
    num_list = [12, 15, 17, 19, 20, 21, 21, 24, 45, 67] #[20, 17, 15, 14, 13, 12, 10, 9, 8, 4]
    target_num = 21
    print(driver(num_list, target_num))
