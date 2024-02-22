# true selection sort algorithm
def selection_sort(array):
    for i in range(len(array)):
        switch_pos = i
        for ii in range(i, len(array)):
            if array[ii] < array[switch_pos]:
                switch_pos = ii
        array[i], array[switch_pos] = array[switch_pos], array[i]
    return array
