example_array = [0, 1, 43, 3, 2, 55, 7, 0, 23, 4]
# print(example_array)

# works in the same way as the bubble sort algorithm, but is inefficient
"""
while True:
    pos = 0
    done = 0
    for i in example_array:
        if pos != len(example_array)-1:
            if i < example_array[pos+1]:
                done += 1
            else:
                example_array[pos], example_array[pos+1] = example_array[pos+1], i
        pos += 1
    if pos-1 == done:
        break
"""

# true bubble sort algorithm
for n in range(len(example_array)):
    for i in range(len(example_array)-1):
        if example_array[i] > example_array[i+1]:
            example_array[i], example_array[i+1] = example_array[i+1], example_array[i]
            print(example_array)

print(example_array)
print('done')
