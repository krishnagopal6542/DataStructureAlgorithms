"""
Topic: Sliding Window
Problem: https://www.geeksforgeeks.org/problems/max-sum-subarray-of-size-k5313/1
"""


def max_sum_subarray(arr, size):
    i, j = 0, 0
    sum, mx = 0, 0

    while j < len(arr):
        sum += arr[j]
        if j - i + 1 == size:
            mx = max(mx, sum)
            sum -= arr[i]
            i += 1
        j += 1
    return mx


if __name__ == '__main__':
    num_list = [100, 200, 300, 400]
    window = 2
    print(max_sum_subarray(num_list, window))
