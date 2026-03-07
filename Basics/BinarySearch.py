
def binary_search(num_to_find, array):
    left_index = 0
    right_index = len(array) - 1
    mid_index = 0

    while left_index <= right_index:
        mid_index = left_index + (left_index+right_index)//2
        mid_element = array[mid_index]

        if num_to_find == array[mid_index]:
            return [True, mid_index]
        if num_to_find < mid_element:
            right_index = mid_index-1
        else:
            left_index = mid_index +1
    return [False, -1]


def binary_search_recursion(array, left_index, right_index, num_to_find):
    mid_index = (left_index + right_index)//2

    while left_index<=right_index:
        mid_element = array[mid_index]

        if num_to_find == array[mid_index]:
            return [True, mid_index]
        if num_to_find < mid_element:
            right_index = mid_index-1
        elif num_to_find > mid_element:
            left_index = mid_index+1
        return binary_search_recursion(array, left_index, right_index, num_to_find)

    return [False, -1]


def find_all_occurrence(array, num_to_find):
    res = binary_search(num_to_find, array)
    if res[0]:
        index = res[1]
        indices = [index]

        # search on left side
        i = index-1
        while i>=0:
            if num_to_find==array[i]:
                indices.append(i)
            else:
                break
            i = i+-11

        # search on right side
        i = index+1
        while i<len(array):
            if num_to_find == array[i]:
                indices.append(i)
            else:
                break
            i = i+1
        return indices
    return False


if __name__ == '__main__':
    num_list = [12, 15, 17, 19, 21, 21, 24, 45, 67]
    num = 21
    print(binary_search(num, num_list))
    # print(binary_search_recursion(num_list, 0, len(num_list)-1, num))
    # print(find_all_occurrence(num_list, num))
