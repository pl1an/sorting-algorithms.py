def bubble_step(array, loopnumber):
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            array[i], array[i + 1] = array[i + 1], array[i]

def insertion_step(array, loopnumber):
    key = array[loopnumber]
    j = loopnumber - 1
    while j >= 0 and key < array[j]:
        array[j + 1] = array[j]
        j -= 1
    array[j + 1] = key

def selection_step(array, loopnumber):
    switch_pos = loopnumber
    for ii in range(loopnumber, len(array)):
        if array[ii] < array[switch_pos]:
            switch_pos = ii
    array[loopnumber], array[switch_pos] = array[switch_pos], array[loopnumber]