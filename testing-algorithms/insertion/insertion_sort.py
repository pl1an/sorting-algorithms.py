# true insertion sort algorithm
def insertion_sort(array):
    for n in range(len(array)):
        key = array[n]
        j = n - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array
