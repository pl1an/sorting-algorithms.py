# testing pivot choices for use in quick sort
example_array = [0, 1, 43, 3, 2, 55, -2, -4, 55, 7, 0, 23, 4, -1]
print(example_array)

# quick sort has variations depending on how you choose the first pivot
# here, it will be picked randomly
# works, but it's inefficient in space since it has to create a temporary array
"""
from random import randint
pivot_choice = randint(0, len(example_array) - 1)
temp_array = [example_array[pivot_choice]]
for i in range(len(example_array)):
    if i != pivot_choice:
        if example_array[i] > example_array[pivot_choice]:
            temp_array.append(example_array[i])
        else:
            temp_array.insert(0, example_array[i])
example_array = temp_array
"""

# This is Hoare's approach to partitioning
# quick sort has variations depending on how you choose the first pivot
# here, it will always be the first value in the array
# this code also only modifies the already existing array, saving space
# (for more info about Hoare's and Lomuto's partition scheme, use the source material)
"""
pivot_choice = 0
count = -1
max_iterations = len(example_array) -1
while count != max_iterations:
    count += 1
    if count != pivot_choice:
        if example_array[count]<example_array[pivot_choice]:
            example_array.insert(0, example_array[count])
            example_array.pop(count + 1)
            pivot_choice += 1
        else:
            example_array.append(example_array[count])
            example_array.pop(count)
            max_iterations -= 1
            count -= 1
"""

# This is also Hoare's approach to partitioning
# does the same thing as the above code, but is a bit more optimized
"""
pivot = example_array[0]
count = -1
max_iterations = len(example_array) -1
while count != max_iterations:
    count += 1
    if example_array[count]<pivot:
        example_array.insert(0, example_array[count])
        example_array.pop(count + 1)
    else:
        example_array.append(example_array[count])
        example_array.pop(count)
        max_iterations -= 1
        count -= 1
"""

# This is Lomuto's approach to partitioning
# Lomuto's partition scheme works best if we decide that the pivot will be the first element of the array by default
# Lomuto's approach is simpler to implement, but it's also slower than Hoare's overall,
# since it may loop through already partitioned elements
smaller_elements = 0
for i in range(len(example_array)):
    if example_array[i] < example_array[0]:
        example_array[i], example_array[smaller_elements+1] = example_array[smaller_elements+1], example_array[i]
        smaller_elements += 1
example_array[0], example_array[smaller_elements] = example_array[smaller_elements], example_array[0]

print(example_array)
print('done')
