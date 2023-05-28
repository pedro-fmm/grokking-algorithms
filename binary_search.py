# Using binary search We can reduce the complexity of a search in a list from O n to O log n

def binary_search(data, item):
    begin = 0
    end = len(data) - 1

    while begin <= end:
        middle = (begin + end) // 2
        if data[middle] == item:
            return middle
        if data[middle] > item:
            end = middle - 1
        else:
            begin = middle + 1 
    return None

my_list = list(range(100))

print(binary_search(my_list, 46))