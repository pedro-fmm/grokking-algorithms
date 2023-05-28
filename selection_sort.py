# using this algorithm we can sort an array by iterating the array and appending the smaller number to other array

def get_smaller(arr):
    smaller = arr[0]
    i_smaller = 0
    for i in range(1, len(arr)):
        if arr[i] < smaller:
            smaller = arr[i]
            i_smaller = i
    return i_smaller

def selection_sort(arr):
    new_arr = []
    for i in range(len(arr)):
        smaller = get_smaller(arr)
        new_arr.append(arr.pop(smaller))
    return new_arr

from random import shuffle

my_array = list(range(10)); shuffle(my_array)

print(my_array)
print(selection_sort(my_array))