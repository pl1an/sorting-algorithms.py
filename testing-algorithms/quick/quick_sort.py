def partition(array, left_limit, right_limit):
    pivot = array[right_limit]
    i = left_limit - 1
    for j in range(left_limit, right_limit):
        if array[j] <= pivot:
            i = i + 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[right_limit] = array[right_limit], array[i + 1]
    return i + 1


# true recursive quick sort algorithm
def quicksort(array, left_limit, right_limit):
    if left_limit < right_limit:
        pi = partition(array, left_limit, right_limit)
        quicksort(array, left_limit, pi - 1)
        quicksort(array, pi + 1, right_limit)