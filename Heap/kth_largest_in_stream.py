import heapq


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.min_heap = []

        for element in nums:
            heapq.heappush(self.min_heap, element)
            if len(self.min_heap) > k:
                heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val)
        while len(self.min_heap) > k:
            heapq.heappop(self.min_heap)

        return heapq.heappop(self.min_heap)

if __name__ == '__main__':
    obj = KthLargest(k, nums)