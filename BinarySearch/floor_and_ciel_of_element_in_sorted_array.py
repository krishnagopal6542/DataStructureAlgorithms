def find_floor_of_element(array, target):
    start, end = 0, len(array) - 1
    floor = -1
    while start <= end:
        mid = start + (end - start) // 2
        if array[mid] <= target:
            floor = array[mid]
            start = mid + 1
        elif array[mid] > target:
            end = mid - 1
    return floor


def find_ciel_of_element(array, target):
    start, end = 0, len(array) - 1
    ciel = -1
    while start <= end:
        mid = start + (end - start) // 2
        if array[mid] >= target:
            ciel = array[mid]
            end = mid - 1
        elif array[mid] < target:
            start = mid + 1
    return ciel


if __name__ == '__main__':
    num = [1, 3, 5, 6]
    element = 2
    print(find_floor_of_element(num, element))
    print(find_ciel_of_element(num, element))
