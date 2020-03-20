from random import randint

def merge(al, ar):
	array0 = []
	lIndex = rIndex = 0
	

	while lIndex < len(al) and rIndex < len(ar):
		if al[lIndex] < ar[rIndex]:
			array0.append(al[lIndex])
			lIndex +=1
		else:
			array0.append(ar[rIndex])
			rIndex +=1
	array0.extend(al[lIndex:])
	array0.extend(ar[rIndex:])
	return array0




def mergeSort(array):
	if len(array) <= 1:
		return array
	middle = len(array)//2
	left, right = mergeSort(array[:middle]), mergeSort(array[middle:])
	return merge(left, right)
	
	


array = [5, 4, 3, 2, 1]


print(f"unsorted array:{array}")
print(mergeSort(array))