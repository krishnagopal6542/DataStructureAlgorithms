def search_on_reverse_sorted_array(array, target):
    start = 0
    end = len(array)-1
    mid_index = 0

    while start<=end:
        mid_index = start + (end-start)//2
        mid_element = array[mid_index]

        if target == mid_element:
            return [True, mid_index]
        if target < mid_element:
            start = mid_index+1
        else:
            end = mid_index-1
    return [False, -1]


if __name__ == '__main__':
    num_list = [20, 17, 15, 14, 13, 12, 10, 9, 8, 4]
    num_to_find = 4
    res = search_on_reverse_sorted_array(num_list, num_to_find)
    print(res)