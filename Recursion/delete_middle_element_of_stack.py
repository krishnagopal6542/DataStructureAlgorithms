def solve(arr, k):
    if k == 1:
        arr.pop()
        return
    temp = arr.pop()
    solve(arr, k - 1)
    arr.append(temp)


def delete_middle_element(arr):
    if len(arr) == 0:
        return
    k = len(arr) // 2 + 1
    solve(arr, k)


if __name__ == '__main__':
    num = [5, 4, 3, 2, 1]
    delete_middle_element(num)
    print(num)
