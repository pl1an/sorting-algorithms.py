example_array = [0, 1, 43, 3, 2, 55, 55, 7, 0, 23, 4, -1]
# print(example_array)

# does not work
# the code runs multiple times through already sorted data changes their order
# the result is the array stays in the same initial order,
# except for all instances of the lowest value, that go to the end of the array
"""
pos = -1
for i in range(len(example_array)):
    pos += 1
    lowest = example_array[pos]
    switch_pos = pos
    for ii in range(len(example_array)):
        if example_array[ii] < lowest:
            lowest = example_array[ii]
            switch_pos = ii
    example_array[pos], example_array[switch_pos] = example_array[switch_pos], example_array[pos]
"""

# the code no longer run's through already sorted data
# with this error fixed, it works exactly as a selection sort algorithm
# but this version is still inefficient in lines of code and rather confusing to read
"""
pos = -1
for i in range(len(example_array)):
    pos += 1
    lowest = example_array[pos]
    switch_pos = pos
    for ii in range(len(example_array[pos::])):
        if example_array[pos::][ii] < lowest:
            lowest = example_array[pos::][ii]
            switch_pos = ii + pos
    example_array[pos], example_array[switch_pos] = example_array[switch_pos], example_array[pos]
"""

# true selection sort algorithm
# removed 3 variables and simplified indentation
for i in range(len(example_array)):
    switch_pos = i
    for ii in range(i, len(example_array)):
        if example_array[ii] < example_array[switch_pos]:
            switch_pos = ii
    example_array[i], example_array[switch_pos] = example_array[switch_pos], example_array[i]
    # print(example_array)

print(example_array)
print('done')
