import heapq


def kth_largest_element(array, k):
    min_heap = []

    for element in array:
        heapq.heappush(min_heap, element)
        if len(min_heap) > k:
            heapq.heappop(min_heap)

    largest_element = heapq.heappop(min_heap)

    print("largest_element ==> ", largest_element)


if __name__ == '__main__':
    nums = [7, 10, 4, 3, 20, 15]
    kth_largest_element(nums, 3)
