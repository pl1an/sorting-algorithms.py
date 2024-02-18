example_array = [1, 43, 3, 4, 2, 55, 7, 77, 0, 23, 4, 0]
# print(example_array)

# simply does not work.
# has a problem sorting situations like [1,3,4,2] - 4 will be removed, but 3 won't
"""
temp_list = []
for i in range(len(example_array)-1):
    if example_array[i]<example_array[i+1]:
        temp_list.append(example_array[i])
        print(temp_list)
example_array = temp_list
"""

# works properly, but it´s slower than the actual stalin sort.
# it's slower because it removes one element and then loops again through the entire array.
# also a lower value in the end of the array will cause the deletion of all the higher values before them,
# while in true stalin sort it would be deleted instead, which might cause a bigger loss of data
# example: [30, 31, 32, 4, 50, 55, 0, 1] -> [0, 1]
"""
def sorted(ar):
    for i in range(0, len(ar) - 1):
        if ar[i] > ar[i + 1]: return False
    return True
    
while not sorted(example_array):
    for i in range(len(example_array)-1):
        if example_array[i]>example_array[i+1]:
            example_array.pop(i)
            print(example_array)
            break
"""

# true stalin sort
# a higher value in the beginning of the array will cause deletion of all lower values after them
# example: [0, 1, 55, 2, 3, 4] -> [0, 1, 55]
max_val = example_array[0]
example_array = [max_val := x for x in example_array if x >= max_val]

print(example_array)
print('done')
