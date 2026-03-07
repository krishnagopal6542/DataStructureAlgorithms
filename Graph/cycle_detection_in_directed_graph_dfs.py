class CycleDetector:
    def dfs(self, node, adj_list, curr_path, visited):
        visited[node] = 1
        curr_path[node] = 1

        for neighbour in adj_list[node]:
            if not visited[neighbour]:
                res = self.dfs(neighbour, adj_list, curr_path, visited)
                if res:
                    return True
            else:
                if curr_path[neighbour] == 1:
                    return True
        curr_path[node] = 0
        return False

    def is_cycle(self, v, adj_list):
        current_path = [0] * v
        visited = [0] * v

        for i in range(v):
            if not visited[i]:
                ans = self.dfs(i, adj_list, current_path, visited)
                if ans:
                    return True
        return False


if __name__ == '__main__':
    CD = CycleDetector()
    test_cases = [
        {
            "name": "Graph with cycle",
            "V": 4,
            "adj": [
                [1],  # 0 -> 1
                [2],  # 1 -> 2
                [0, 3],  # 2 -> 0, 3 (cycle: 0->1->2->0)
                []  # 3 -> nothing
            ],
            "expected": True
        },
        {
            "name": "DAG (no cycle)",
            "V": 4,
            "adj": [
                [1, 2],  # 0 -> 1, 2
                [2],  # 1 -> 2
                [3],  # 2 -> 3
                []  # 3 -> nothing
            ],
            "expected": False
        },
        {
            "name": "Self-loop",
            "V": 3,
            "adj": [
                [1],  # 0 -> 1
                [1, 2],  # 1 -> 1 (self-loop), 2
                []  # 2 -> nothing
            ],
            "expected": True
        },
        {
            "name": "Disconnected graph with cycle",
            "V": 6,
            "adj": [
                [1],  # 0 -> 1
                [2],  # 1 -> 2
                [],  # 2 -> nothing
                [4],  # 3 -> 4
                [5],  # 4 -> 5
                [3]  # 5 -> 3 (cycle: 3->4->5->3)
            ],
            "expected": True
        },
        {
            "name": "Linear chain (no cycle)",
            "V": 5,
            "adj": [
                [1],  # 0 -> 1
                [2],  # 1 -> 2
                [3],  # 2 -> 3
                [4],  # 3 -> 4
                []  # 4 -> nothing
            ],
            "expected": False
        },
        {
            "name": "Complex graph with cycle",
            "V": 5,
            "adj": [
                [1, 2],  # 0 -> 1, 2
                [3],  # 1 -> 3
                [3],  # 2 -> 3
                [4],  # 3 -> 4
                [1]  # 4 -> 1 (cycle: 1->3->4->1)
            ],
            "expected": True
        },
        {
            "name": "Single node (no cycle)",
            "V": 1,
            "adj": [
                []  # 0 -> nothing
            ],
            "expected": False
        },
        {
            "name": "Two nodes with cycle",
            "V": 2,
            "adj": [
                [1],  # 0 -> 1
                [0]  # 1 -> 0 (cycle: 0->1->0)
            ],
            "expected": True
        },
        {
            "name": "Multiple disconnected cycles",
            "V": 8,
            "adj": [
                [1],  # 0 -> 1
                [0],  # 1 -> 0 (cycle 1: 0->1->0)
                [3],  # 2 -> 3
                [4],  # 3 -> 4
                [2],  # 4 -> 2 (cycle 2: 2->3->4->2)
                [6],  # 5 -> 6
                [7],  # 6 -> 7
                []  # 7 -> nothing (no cycle)
            ],
            "expected": True
        },
        {
            "name": "Star graph (no cycle)",
            "V": 5,
            "adj": [
                [1, 2, 3, 4],  # 0 -> 1, 2, 3, 4
                [],  # 1 -> nothing
                [],  # 2 -> nothing
                [],  # 3 -> nothing
                []  # 4 -> nothing
            ],
            "expected": False
        }
    ]
    print("=" * 70)
    print("RUNNING ALL TEST CASES FOR DIRECTED GRAPH CYCLE DETECTION")
    print("=" * 70)
    print()

    passed = 0
    failed = 0

    for i, test in enumerate(test_cases, 1):
        print(f"Test Case {i}: {test['name']}")
        print(f"Vertices: {test['V']}")
        print(f"Adjacency list: {test['adj']}")

        result = CD.is_cycle(test['V'], test['adj'])
        expected = test['expected']

        status = "✓ PASS" if result == expected else "✗ FAIL"
        if result == expected:
            passed += 1
        else:
            failed += 1

        print(f"Expected: {expected}, Got: {result} - {status}")
        print("-" * 70)
        print()

    print("=" * 70)
    print(f"SUMMARY: {passed} passed, {failed} failed out of {len(test_cases)} tests")
    print("=" * 70)
    print()
