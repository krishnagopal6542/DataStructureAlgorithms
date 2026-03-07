import heapq


def get_kth_smallest_element(array, k):
    max_heap = []

    for element in array:
        heapq.heappush(max_heap, -element)
        if len(max_heap) > k:
            heapq.heappop(max_heap)

    kth_smallest_element = -heapq.heappop(max_heap)
    return kth_smallest_element


def sum_of_element_k1th_k2th(array, k1, k2):
    k1_val = get_kth_smallest_element(array, k1)
    k2_val = get_kth_smallest_element(array, k2)

    element_sum = 0
    for element in array:
        if k1_val < element < k2_val:
            element_sum += element

    return element_sum

if __name__ == '__main__':
    num = [1, 3, 12, 5, 15, 11]
    k1 = 3
    k2 = 6
    print(sum_of_element_k1th_k2th(num, k1, k2))
