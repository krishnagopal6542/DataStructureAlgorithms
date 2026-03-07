def bubble_sort(elements):
    size = len(elements)

    for i in range(size-1):
        swapped = True
        for j in range(size-1-i):
            if elements[j] > elements[j+1]:
                elements[j], elements[j+1] = elements[j+1], elements[j]
            if not swapped:
                break


def bubble_sort_func(arr_obj, key):
    size = len(arr_obj)

    for i in range(size-1):
        swapped = True
        for j in range(size-1-i):
            if arr_obj[j][key] > arr_obj[j+1][key]:
                arr_obj[j], arr_obj[j+1] = arr_obj[j+1], arr_obj[j]
        if not swapped:
            break



if __name__ == '__main__':
    element = [5,9,2,1,67,34,88,34]
    bubble_sort(element)
    print(element)

    ele_obj = [
        {'name': 'mona', 'transaction_amount': 1000, 'device': 'iphone-10'},
        {'name': 'krish', 'transaction_amount': 400, 'device': 'google pixel'},
        {'name': 'kathy', 'transaction_amount': 200, 'device': 'samsung'},
        {'name': 'aamir', 'transaction_amount': 800, 'device': 'iphone-8'},
    ]
    bubble_sort_func(ele_obj, 'transaction_amount')
    for element in ele_obj:
        print(element)