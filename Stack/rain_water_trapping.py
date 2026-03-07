"""
Leet code: 42
This is different from Maximum are a Histogram problem.
Here we don't find NSL or NSR, rather we find absolutely greater to left and right.
"""


def max_left(array):
    max_l = [0] * len(array)
    for i in range(len(array)):
        max_l[i] = max(max_l[i - 1], array[i])
    return max_l


def max_right(array):
    max_r = [0] * len(array)
    j = len(array) - 1
    right_max = 0
    while j >= 0:
        right_max = max(right_max, array[j])
        max_r[j] = right_max
        j -= 1
    return max_r


def water_on_building(array):
    max_l = max_left(array)
    max_r = max_right(array)
    water = [0] * len(array)
    total_water = 0

    for i in range(len(array) - 1):
        water[i] = min(max_r[i], max_l[i]) - array[i]
        total_water += water[i]
    return total_water


if __name__ == '__main__':
    num = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(water_on_building(num))
