def selectionSort(array):
    for x in range(len(array)):
        for y in range(x, len(array)):
            if array[y] < array[x]:
                array[y], array[x] = array[x], array[y]
            
array = [5, 4, 3, 2, 1]
selectionSort(array)
print(array)