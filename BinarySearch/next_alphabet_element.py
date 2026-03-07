def next_greatest_letter(letters, target):
    start, end = 0, len(letters) - 1
    res = letters[0]
    while start <= end:
        mid = start + (end - start) // 2
        if ord(letter[mid]) <= ord(target):
            start = mid + 1
        elif ord(letter[mid]) > ord(target):
            res = letter[mid]
            end = mid - 1
    return res


if __name__ == '__main__':
    letter = ["c", "f", "j"]
    element = "j"
    print(next_greatest_letter(letter, element))
