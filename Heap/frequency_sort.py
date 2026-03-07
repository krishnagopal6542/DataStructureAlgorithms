# Leet code: 1636
import heapq


def sort_by_increasing_frequency(array):
    _map = {}
    for element in array:
        _map[element] = _map.get(element, 0) + 1

    min_heap = []
    for key, frequency in _map.items():
        heapq.heappush(min_heap, (frequency, key))

    res = []

    while min_heap:
        top = heapq.heappop(min_heap)
        frequency, key = top[0], top[1]
        for i in range(frequency):
            res.append(key)

    return res


def sort_by_decreasing_frequency(array):
    _map = {}
    for element in array:
        _map[element] = _map.get(element, 0) + 1

    max_heap = []
    for key, frequency in _map.items():
        heapq.heappush(max_heap, (-frequency, key))

    res = []
    while max_heap:
        top = heapq.heappop(max_heap)
        frequency, key = -top[0], top[1]
        for i in range(frequency):
            res.append(key)

    return res


if __name__ == '__main__':
    nums = [2, 3, 1, 3, 2]
    print(sort_by_decreasing_frequency(nums))
