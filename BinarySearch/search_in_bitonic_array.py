"""
A Bitonic Sequence is a sequence of numbers that is first strictly increasing then after a point decreasing.
Leet code: 1095
"""


def get_peak_element(array):
    low, high = 0, len(array) - 1
    if len(array) == 1:
        return 0
    while low <= high:
        mid = low + (high - low) // 2
        if 0 < mid < len(array) - 1:
            if array[mid] > array[mid - 1] and array[mid] > array[mid + 1]:
                return mid
            elif array[mid] < array[mid + 1]:
                low = mid + 1
            else:
                high = mid - 1
        elif mid == 0:
            return mid if array[mid] > array[mid + 1] else mid + 1
        elif mid == len(array) - 1:
            return mid if array[mid] > array[mid - 1] else mid - 1
    return None


def search_in_increasing_array(array, start, end, target):
    while start <= end:
        mid = start + (end - start) // 2
        if target == array[mid]:
            return mid
        elif array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return -1


def search_in_descending_array(array, start, end, target):
    while start <= end:
        mid = start + (end - start) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            end = mid - 1
        else:
            start = mid + 1
    return -1


def driver(array, target):
    get_peak_element(array)
    # peak_element_index = get_peak_element(array)
    # res = search_in_increasing_array(array, 0, peak_element_index, target)
    # return res if res > 0 else search_in_descending_array(array, peak_element_index + 1, len(array) - 1, target)


if __name__ == '__main__':
    num = [1, 2, 3, 4, 5, 3, 1]
    n = 3
    print(driver(num, n))
