from random import randint
def sorted(ar):
    for i in range(0, len(ar) - 1):
        if ar[i] > ar[i + 1]:
            return False
    return True


def bubble_step(array, loopnumber):
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            array[i], array[i + 1] = array[i + 1], array[i]
    return loopnumber+1

def insertion_step(array, loopnumber):
    key = array[loopnumber]
    j = loopnumber - 1
    while j >= 0 and key < array[j]:
        array[j + 1] = array[j]
        j -= 1
    array[j + 1] = key
    return loopnumber+1

def selection_step(array, loopnumber):
    switch_pos = loopnumber
    for ii in range(loopnumber, len(array)):
        if array[ii] < array[switch_pos]:
            switch_pos = ii
    array[loopnumber], array[switch_pos] = array[switch_pos], array[loopnumber]
    return loopnumber+1

def bozo_step(array, loopnumber):
    a = randint(0, len(array)-1)
    b = randint(0, len(array) - 1)
    array[a], array[b] = array[b], array[a]
    if(sorted(array)):
        loopnumber = len(array)
    else:
        loopnumber = 0
    return loopnumber+1

def bogo_step(array, loopnumber):
    for i in range(len(array)):
        n = randint(0, len(array) - 1)
        array[i], array[n] = array[n], array[i]
    if(sorted(array)):
        loopnumber = len(array)
    else:
        loopnumber = 0
    return loopnumber+1
