import heapq


def k_closest_element(array, K, X):
    max_heap = []

    for i in range(len(array)):
        abs_diff = abs(X - array[i])
        heapq.heappush(max_heap, (-abs_diff, -array[i]))
        if len(max_heap) > K:
            heapq.heappop(max_heap)

    res = []

    while max_heap:
        res.append(-heapq.heappop(max_heap)[1])

    res.sort()
    print("res ==> ", res)

    return res


if __name__ == '__main__':
    arr = [1,2,3,4,5]
    k = 4
    x = 3
    k_closest_element(arr, k, x)
