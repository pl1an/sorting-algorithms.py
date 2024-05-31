from random import randint

#creates an array of lenght "leng"
def generate_data(leng):
    data = []
    for i in range(0, leng):
        data.append(i)
    return data

#shuffles an array up to "max_shuffles" times
def shuffle(target_array, max_shuffles):
    array = target_array
    for i in range(0, max_shuffles):
        p1, p2 = randint(0, len(array)-1), randint(0, len(array)-1)
        array[p1], array[p2] = array[p2], array[p1]
    return array