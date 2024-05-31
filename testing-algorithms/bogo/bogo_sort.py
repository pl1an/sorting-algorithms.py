def sorted(ar):
    for i in range(0, len(ar) - 1):
        if ar[i] > ar[i + 1]: return False
    return True

# true bogo sort algorithm
def bogo_sort(array):
    import random
    while not sorted(array):
        for i in range(len(array)):
            n = random.randint(0, len(array) - 1)
            array[i], array[n] = array[n], array[i]
    return array
