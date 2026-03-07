import heapq


def k_closest_element(array, X, K):
    max_heap = []

    for element in array:
        abs_diff = abs(X - element)
        heapq.heappush(max_heap, (-abs_diff, -element))
        if len(max_heap) > K:
            heapq.heappop(max_heap)

    res = []
    while max_heap:
        top = -heapq.heappop(max_heap)[1]
        res.append(top)
    res.sort()
    return res


if __name__ == '__main__':
    arr = [5, 6, 7, 8, 9]
    k = 3
    x = 7
    print(k_closest_element(arr, x, k))
