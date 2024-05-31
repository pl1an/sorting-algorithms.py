import random

example_array = [0, 1, 43, 3, 2, 55, 7, 0, 23, 4]
print(example_array)

def sorted(ar):
    for i in range(0, len(ar) - 1):
        if ar[i] > ar[i + 1]: return False
    return True

# this is not exactly bogo sort, since it just switches elements randomly instead of shuffling the whole array
# this is actually called bozo sort
"""
while sorted(example_array) == False:
    a = random.randint(0, len(example_array)-1)
    b = random.randint(0, len(example_array) - 1)
    example_array[a], example_array[b] = example_array[b], example_array[a]
"""

# true bogo sort algorithm
while not sorted(example_array):
    for i in range(len(example_array)):
        n = random.randint(0, len(example_array)-1)
        example_array[i], example_array[n] = example_array[n], example_array[i]
    # print(example_array)

print(example_array)
print('done')
