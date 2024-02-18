import random

example_array = [0, 1, 43, 3, 2, 55, 7, 0, 23, 4]
print(example_array)

def sorted(ar):
    for i in range(0, len(ar) - 1):
        if ar[i] > ar[i + 1]:
            return False
    return True

# true bozo sort? couldn't find any examples in python
while not sorted(example_array):
    a = random.randint(0, len(example_array)-1)
    b = random.randint(0, len(example_array) - 1)
    example_array[a], example_array[b] = example_array[b], example_array[a]
