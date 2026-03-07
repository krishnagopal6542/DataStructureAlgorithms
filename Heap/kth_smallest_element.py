import heapq


def kth_smallest_element(array, k):
    max_heap = []
    for element in array:
        heapq.heappush(max_heap, -element)
        if len(max_heap) > k:
            heapq.heappop(max_heap)

    smallest_element = -heapq.heappop(max_heap)

    print("smallest_element ==> ", smallest_element)


def kth_smallest_element_for_matrix(array, k):
    max_heap = []
    for i in range(len(array)):
        for j in range(len(array[i])):
            heapq.heappush(max_heap, -array[i][j])
            if len(max_heap) > k:
                heapq.heappop(max_heap)

    smallest_element = -heapq.heappop(max_heap)

    print("smallest_element ==> ", smallest_element)


if __name__ == '__main__':
    matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
    k = 8
    kth_smallest_element_for_matrix(matrix, k)
