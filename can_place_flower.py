"""
605. Can Place Flowers
"""
from typing import List


class Solution:
    def can_place_flowers(self, flowerbed: List[int], n: int) -> bool:
        if n <= 0:
            return True

        for i in range(len(flowerbed)):
            if flowerbed[i] == 0 and (i==0 or flowerbed[i-1] == 0) and (i<len(flowerbed)-1 or flowerbed[i+1]==0):
                flowerbed[i] = 1 #Plant Tree
                n -= 1
                if n <= 0:
                    return True

        return n <= 0


if __name__ == '__main__':
    FlowerBed = [1,0,0,0,1,0,0]
    N = 2
    print(Solution().can_place_flowers(flowerbed=FlowerBed, n=N))
