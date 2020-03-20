def bubbleSort(array):
    for x in range(len(array)):
        for y in range(len(array)-x-1):
            if array[y] > array[y+1]:
                array[y], array[y+1] = array[y+1], array[y]
        
array = [5, 4, 3, 2, 1]
bubbleSort(array)
print(array)