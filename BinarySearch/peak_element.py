def get_peak_element(array):
    start, end = 0, len(array) - 1

    if len(array) == 1:
        return 0

    while start <= end:
        mid = start + (end - start) // 2
        if 0 < mid < len(array) - 1:
            if array[mid] > array[mid - 1] and array[mid] > array[mid + 1]:
                return mid
            elif array[mid] < array[mid + 1]:
                start = mid + 1
            else: 
                end = mid - 1
        elif mid == 0:
            return mid if array[mid] > array[mid + 1] else mid + 1
        elif mid == len(array) - 1:
            return mid if array[mid] > array[mid - 1] else mid - 1
    return -1


if __name__ == '__main__':
    num = [6, 5, 4, 3, 2, 3, 2]
    print(get_peak_element(num))
