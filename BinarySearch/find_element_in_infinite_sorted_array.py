"""
This is the kind of problem that we can't solve, because infinite will not be available practically.
So we will start figuring out if the key is in the range.
Once we find the bound withing the array, then we can apply binary search on that array with the low and high bound.
"""


def binary_search(start, end, array, target):
    while start <= end:
        mid = start + (end - start) // 2
        if array[mid] == target:
            return mid
        elif target > array[mid]:
            start + mid + 1
        elif target < array[mid]:
            end = mid - 1
    return -1


def find_in_infinite_sorted_array(array, target):
    low, high = 0, 1
    while target > array[high]:
        low = high
        high = high * 2
    return binary_search(low, high, array, target)


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    key = 7
    print(find_in_infinite_sorted_array(nums, key))
