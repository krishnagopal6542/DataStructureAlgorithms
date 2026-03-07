import heapq


def minimise_rope_cost(array):
    min_heap = []
    cost = 0

    for element in array:
        heapq.heappush(min_heap, element)
    print(min_heap)

    while len(min_heap) >= 2:
        first = heapq.heappop(min_heap)
        second = heapq.heappop(min_heap)

        cost = cost + first + second

        heapq.heappush(min_heap, first + second)

    return cost


if __name__ == '__main__':
    num = [1, 2, 3, 4, 5]
    print(minimise_rope_cost(num))
