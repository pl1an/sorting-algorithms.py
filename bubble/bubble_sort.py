# true bubble sort algorithm
def bubble_sort(array):
    for n in range(len(array)):
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                print(array)
    return array
