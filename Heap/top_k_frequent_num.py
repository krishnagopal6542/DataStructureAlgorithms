import heapq


def top_ke_frequent_element(array, K):
    _map = {}

    for element in array:
        if element in _map:
            _map[element] += 1
        else:
            _map[element] = 1

    min_heap = []

    for key, value in _map.items():
        print(key, value)
        heapq.heappush(min_heap, (value, key))
        if len(min_heap) > k:
            heapq.heappop(min_heap)

    res = []

    while min_heap:
        top = heapq.heappop(min_heap)
        res.append(top[1])

    return res


if __name__ == '__main__':
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    print(top_ke_frequent_element(nums, k))
