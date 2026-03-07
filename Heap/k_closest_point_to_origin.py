import heapq


def kth_closest_point_to_origin(array, K):
    max_heap = []

    for i in range(len(array)):
        x, y = array[i][0], array[i][1]
        square = x * x + y * y
        heapq.heappush(max_heap, (-square, [x, y]))
        if len(max_heap) > K:
            heapq.heappop(max_heap)

    res = []

    while max_heap:
        top = heapq.heappop(max_heap)
        res.append(top[1])

    return res


if __name__ == '__main__':
    points = [[3,3],[5,-1],[-2,4]]
    k = 2
    print(kth_closest_point_to_origin(points, k))
