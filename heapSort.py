from random import randint

def swap(array, i1, i2):
    array[i1], array[i2] = array[i2], array[i1]

def heapify(array, start, end):
    left = 2 * start + 1
    right = 2 * start + 2
    print(array, start)
    if right <= end:
        heapify(array, left, end)
        heapify(array, right, end)
        if array[start] < array[left] or array[start] < array[right]:
            if array[left] < array[right]:
                swap(array, start, right)
                heapify(array, right, end)
            else:
                swap(array, start, left)
                heapify(array, left, end)
    

def heapSort(array):
    end = len(array) - 1
    heapify(array, 0, end)
    print()
    while end > 0:
        swap(array, 0, end)
        end -= 1
        heapify(array, 0, end)

def main():
    array = []
    for x in range(10):
        array.append(randint(0, 100))
    heapSort(array)
    print(array)

if __name__ == "__main__":
    main()

