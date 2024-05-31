# example_array = [0, 1, 3, 2, -2, -4, 0, 4, -1]
example_array = [0, 1, 3, 10, 2, -2, -4, 7, 0, 9, 4, -1]
print(example_array)


# definitions of Hoare's and Lomuto's partitioning methods
"""
def hoare(array):
    count = -1
    max_iterations = len(array) - 1
    pivot = array[0]
    while count != max_iterations:
        count += 1
        if array[count] < pivot:
            array.insert(0, array[count])
            array.pop(count + 1)
        else:
            array.append(array[count])
            array.pop(count)
            max_iterations -= 1
            count -= 1
    return array, count+1

def lomuto(array):
    smaller_elements = 0
    for i in range(len(array)):
        if array[i] < array[0]:
            array[i], array[smaller_elements + 1] = array[smaller_elements + 1], array[i]
            smaller_elements += 1
    array[0], array[smaller_elements] = array[smaller_elements], array[0]
    return array, smaller_elements
"""

# attempt of replicating quick sort using Hoare's approach
# only works for small arrays, and it's slow, hard to read, unoptimized and overall just... bad
"""
def sorted(array):
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            return False
    return True

left_limit = 0
right_limit = len(example_array)-1
left_pivot_count = 0
right_pivot_count = 0
while not sorted(example_array):
    count = left_limit -1
    pivot = example_array[left_limit]

    hoare_limit = right_limit
    while count != hoare_limit:
        count += 1
        if example_array[count] < pivot:
            example_array.insert(left_limit, example_array[count])
            example_array.pop(count + 1)

        else:
            example_array.insert(right_limit+1,example_array[count])
            example_array.pop(count)
            hoare_limit -= 1
            count -= 1

    if count < right_limit - 1:
        left_pivot_count += 1
    else:
        right_pivot_count += 1

    right_limit = count
    if sorted(example_array[:right_limit+1]):
        left_limit = right_limit+left_pivot_count
        right_limit = len(example_array) - right_pivot_count - 1
        left_pivot_count = 0
        right_pivot_count = 0
    print(example_array)
"""


# partitioning using Lomuto's approach, but maintaining pivot at the end of the array, instead of the beginning
def partition(array, left_limit, right_limit):
    pivot = array[right_limit]
    i = left_limit - 1
    for j in range(left_limit, right_limit):
        if array[j] <= pivot:
            i = i + 1
            array[i], array[j] = array[j], array[i]
            # print(str(array) + "-partitioning")
    array[i + 1], array[right_limit] = array[right_limit], array[i + 1]
    # print(str(array) + "-ending_partition")
    return i + 1


# true recursive quick sort algorithm
def quicksort(array, left_limit, right_limit):
    if left_limit < right_limit:
        pi = partition(array, left_limit, right_limit)
        quicksort(array, left_limit, pi - 1)
        quicksort(array, pi + 1, right_limit)
        # print(str(array) + "-right_recursive")


quicksort(example_array, 0, len(example_array)-1)
print(example_array)
print('done')
