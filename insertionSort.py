def insertionSort(array):
    for x in range(len(array)):
        y = x
        while y > 0 and array[y] < array[y-1]:
            array[y], array[y-1] = array[y-1], array[y]
            y -=1
        
array = [5, 4, 3, 2, 1]
insertionSort(array)
print(array)