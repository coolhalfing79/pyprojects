from random import randint

def swap(array, i1, i2):
    array[i1], array[i2] = array[i2], array[i1]

def heapify(array, start, end):
    left = 2 * start + 1
    right = 2 * start + 2
    largest = start
    print(array, start)
    if start < end:
        heapify(array, right, end)
        heapify(array, left, end)
        if end >= left and array[largest] < array[left]:
            largest = left
        if end >= right and array[largest] < array[right]:
            largest = right
        if largest != start:
            swap(array, start, largest)
            heapify(array, largest, end)
    

def heapSort(array):
    end = len(array) - 1
    while end > 0:
        heapify(array, 0, end)
        swap(array, 0, end)
        end -= 1

def main():
    array = []
    lim = 10
    while len(array) < lim:
        array.append(randint(0, 100))
    heapSort(array)
    print(array)

if __name__ == "__main__":
    main()

