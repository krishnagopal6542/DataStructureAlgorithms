import collections
from typing import List


class Solution:
    def max_sliding_window(self, nums: List[int], k: int) -> List[int]:
        i, j = 0, 0
        max_val = -1
        response = []
        q = collections.deque() # Used to store recent max value, such that when k hits, then q[0] holds max value

        while j < len(nums):
            while q and nums[j] > q[-1]: # q[-1] holds last value in queue, i.e from right
                q.pop()
            q.append(nums[j])

            if j-i+1 == k:
                max_val = q[0]  # q[0] holds first value of the queue, i.e of the left
                response.append(max_val)

                if nums[i] == q[0]:
                    q.popleft()
                i += 1
            j += 1

        return response


if __name__ == '__main__':
    num_array = [1, 3, -1, -3, 5, 3, 6, 7]
    size = 3
    print(Solution().max_sliding_window(nums=num_array, k=size))
