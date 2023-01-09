# Python3 program for implementation of Shell Sort
  
def shellSort(arr):
    gap = len(arr) // 2 # initialize the gap
  
    while gap > 0:
        i = 0
        j = gap
          
        # check the array in from left to right
        # till the last possible index of j
        while j < len(arr):
      
            if arr[i] >arr[j]:
                arr[i],arr[j] = arr[j],arr[i]
              
            i += 1
            j += 1
          
            # now, we look back from ith index to the left
            # we swap the values which are not in the right order.
            k = i
            while k - gap > -1:
  
                if arr[k - gap] > arr[k]:
                    arr[k-gap],arr[k] = arr[k],arr[k-gap]
                k -= 1
  
        gap //= 2
  
  
# driver to check the code
arr = [64, 34, 25, 16, 4, 75, 11, 90, 123, 43, 64, 72]
print("input array:",arr)
  
shellSort(arr)
print("sorted array",arr)

# Time Complexity O(n^2)