# Leet Code:
import collections
from typing import List


class Solution:
    def min_mutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank_set = set(bank)

        q = collections.deque()
        visited = set()
        q.append(startGene)
        visited.add(startGene)

        level = 0

        while q:
            n = len(q)

            for _ in range(n):
                current_word = q.popleft()

                if current_word == endGene:
                    return level

                for ch in "ACGT":
                    for i in range(len(current_word)):
                        neighbour = current_word[:i] + ch + current_word[i + 1:]
                        if neighbour not in visited and neighbour in bank_set:
                            q.append(neighbour)
                            visited.add(neighbour)
            level += 1
        return -1


if __name__ == '__main__':
    start_gene = "AACCGGTT"
    end_gene = "AACCGGTA"
    Bank = ["AACCGGTA"]
    print(Solution().min_mutation(startGene=start_gene, endGene=end_gene, bank=Bank))
