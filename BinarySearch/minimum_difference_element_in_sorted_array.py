"""
https://www.callicoder.com/minimum-difference-element-in-sorted-array/
This is similar to binary search, but here we have to return the element that return the absolute difference.
In order to do so, we need to find both the adjacent element of the target, and then check which element
gives the min value. Return the element that gives min value.

And if the target is present in the array, return the target as the it will only give the absolute min value.
"""


def minimum_difference_element(array, target):
    start, end = 0, len(array) - 1

    if target < array[start]:
        return array[start]
    if target > array[end]:
        return array[end]

    while start <= end:
        mid = start + (end - start) // 2
        if array[mid] == target:
            return array[mid]
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    low_abs_diff = abs(array[start] - target)
    high_abs_diff = abs(array[end] - target)

    return array[start] if low_abs_diff < high_abs_diff else array[end]


if __name__ == '__main__':
    num = [2, 5, 10, 12, 15]
    keys = [6, 5, 8, 11, 20]
    for key in keys:
        print(minimum_difference_element(num, key))
