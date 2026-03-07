def main(array: list[int], k: int):
    i, j = 0, 0
    max_length = 0
    total_subarray = 0
    sum_val = 0

    while j < len(nums):
        sum_val += nums[j]
        if sum_val < k:
            j += 1
        elif sum_val > k:
            while sum_val > k:
                sum_val -= nums[i]
                i += 1
            if sum_val == k:
                max_length = max(max_length, j - i + 1)
                total_subarray += 1
                j += 1
            else:
                j += 1

        elif sum_val == k:
            max_length = max(max_length, j - i + 1)
            total_subarray += 1
            j += 1
    return max_length, total_subarray


if __name__ == '__main__':
    nums = [4, 1, 1, 1, 2, 3, 5]
    Sum = 5
    print(main(array=nums, k=Sum))
