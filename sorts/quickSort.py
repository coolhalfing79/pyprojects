from random import randint


def makePivot(array, start, end):
	pivotIndex = start
	for arrayIndex in range(start, end):
		if array[arrayIndex] < array[end]:
			array[arrayIndex], array[pivotIndex] = array[pivotIndex], array[arrayIndex]
			pivotIndex +=1
	array[end], array[pivotIndex] = array[pivotIndex], array[end]
	return pivotIndex

def quickSort(array, start, end):
	if start >= end :
		return
	pivot = makePivot(array, start, end)
	quickSort(array, start, pivot-1)
	quickSort(array, pivot+1, end)


array = []
for x in range(100):
	array.append(randint(0, 99))

print(f"unsorted array:{array}")
quickSort(array, 0, 99)
print(f"sorted array:{array}")
