def reverse(arr):
    if len(arr) == 1:
        return
    last_element = arr.pop()
    reverse(arr)
    arr.insert(0, last_element)


if __name__ == '__main__':
    num = [1, 2, 3, 4, 5]
    reverse(num)
    print(num)
