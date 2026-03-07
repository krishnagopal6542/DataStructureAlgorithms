# Leet code 35

# def search_position(array, target):
#     start, end = 0, len(array) - 1
#     while start <= end:
#         mid = start + (end - start) // 2
#         if array[mid] == target:
#             return mid
#         elif array[mid] < target:
#             start = mid + 1
#         else:
#             end = mid - 1
#     return -1
#
#
# def insert_position(array, target):
#     start, end = 0, len(array) - 1
#     floor = -1
#     while start <= end:
#         mid = start + (end - start) // 2
#         if array[mid] <= target:
#             floor = mid
#             start = mid + 1
#         elif array[mid] > target:
#             end = mid - 1
#     return floor + 1


def driver(array, target):
    res = search_position(array, target)
    print("res ==> ", res)
    return res if res >= 0 else insert_position(array, target)


def search_position(array, target):
    start, end = 0, len(array) - 1
    while start <= end:
        mid = start + (end - start) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return start


def insert_position(array, target):
    start, end = 0, len(array) - 1
    floor = -1
    while start <= end:
        mid = start + (end - start) // 2
        if array[mid] <= target:
            floor = mid
            start = mid + 1
        elif array[mid] > target:
            end = mid - 1
    return floor + 1


if __name__ == '__main__':
    nums = [1, 3, 5, 6]
    key = 7
    print(search_position(nums, key))