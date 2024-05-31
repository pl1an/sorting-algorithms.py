def sorted(ar):
    for i in range(0, len(ar) - 1):
        if ar[i] > ar[i + 1]:
            return False
    return True

# true bozo sort algorithm
def bozo_sort(array):
    from random import randint
    while not sorted(array):
        a = randint(0, len(array)-1)
        b = randint(0, len(array) - 1)
        array[a], array[b] = array[b], array[a]
    return array
