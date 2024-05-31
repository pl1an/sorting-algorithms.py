example_array = [0, 1, 43, 3, 2, 55, 55, 7, 0, 23, 4, -1]
# print(example_array)

# funny behaviour, works similarly to an insertion algorithm, but it sorts the list twice-ish
# add print(example_array) after line 10 (inside if statement) for better visualization
"""
for n in range(len(example_array)):
    for i in range(len(example_array)):
        if example_array[n]<example_array[i]:
            example_array[n], example_array[i] = example_array[i], example_array[n]
"""

# same strange behaviour as the first code, add print(example_array) after line 22 for visualization
"""
for n in range(len(example_array)):
    mini = example_array[n]
    pos = n
    for i in range(len(example_array)):
        if mini < example_array[i]:
            mini = example_array[i]
            pos = i
            example_array[n], example_array[pos] = example_array[pos], example_array[n]
"""

# true insertion sort algorithm
for n in range(len(example_array)):
    key = example_array[n]
    j = n-1
    while j >= 0 and key < example_array[j]:
        example_array[j+1] = example_array[j]
        j -= 1
    example_array[j + 1] = key
    # print(example_array)

print(example_array)
print('done')
