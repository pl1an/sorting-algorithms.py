# true stalin sort algorithm
def stalin_sort(array):
    max_val = array[0]
    return [max_val := x for x in array if x >= max_val]
