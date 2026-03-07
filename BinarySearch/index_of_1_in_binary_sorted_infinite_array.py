"""
https://www.geeksforgeeks.org/dsa/find-index-first-1-infinite-sorted-array-0s-1s/
It is a combination of two problems
    i.  First occurrence of element in sorted array
    ii. find element in infinite sorted array

first we will find the array bound, i.e lower and upper bound within which element is there and then will implement
First occurrence of element in sorted array
"""


def first_occurrence_of_element(array, low, high, target):
    res = -1
    while low <= high:
        mid = low + (high - low) // 2

        if array[mid] == target:
            res = mid
            high = mid - 1
        elif array[mid] > target:
            end = mid - 1
        elif array[mid] < target:
            low = mid + 1
    return res


def driver(array, target):
    low, high = 0, 1
    while target > array[high]:
        low = high
        high = high * 2

    print("low, high ==> ", low, high)

    return first_occurrence_of_element(array, low, high, target)


if __name__ == '__main__':
    num = [0, 0, 1, 1, 1, 1]
    key = 1
    print(driver(num, key))
