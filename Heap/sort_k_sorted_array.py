import heapq


def sort_k_sorted_array(array, k):
    min_heap = []
    res = []

    for element in array:
        heapq.heappush(min_heap, element)
        if len(min_heap) > k:
            top = heapq.heappop(min_heap)
            res.append(top)

    while min_heap:
        top = heapq.heappop(min_heap)
        res.append(top)

    return res


if __name__ == '__main__':
    num = [6, 5, 3, 2, 8, 10, 9]
    print(sort_k_sorted_array(num, 3))
