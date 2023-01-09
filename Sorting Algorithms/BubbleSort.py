# Python program for implementation of Bubble Sort

def bubbleSort(arr):
	n = len(arr)

	# Traverse through all array elements
	for i in range(n):

		# Last i elements are already in place
		for j in range(0, n-i-1):
			'''
			Traverse the array from 0 to n-i-1
			Swap if the element found is greater
			than the next element 
			'''
			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [64, 34, 25, 16, 4, 75, 11, 90, 123, 43, 64, 72]

bubbleSort(arr)

print("Sorted array list:")
for i in arr:
	print(i)

# Time Complexity O(n^2)
