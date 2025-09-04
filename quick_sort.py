"""
# QuickSort: is a sorting algorithms that uses the divide and conquer that picks
  an element at a pivot and partitions the given array around the picked pivot by
  placing the pivot in its correct position in the sorted array.

# Time complexity:Best case O (n log n ), worst case O(n^2)

# Why use QuickSort:
 pros:
 - very fast: atleast in average case.
 - In-place: saves on memory, doesnot need to do alot of copying and allocating

cons:
 - Povit sensitivity: if the pivot is choosen wrongly it can lead to poor performance.
 - Typically unstable: changes the relative of elements with equal keys.
 - Recursive : can oncur an performance penantly.
"""

def quick_sort(arr, low, high):
    if low >= high:
        return

    pi = partition(arr, low, high)

    quick_sort(arr, low, pi-1)
    quick_sort(arr, pi + 1 , high)


def partition(arr, low, high):

    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i +=1
            arr[i], arr[j] = arr[j] , arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]

    return i + 1




nums =  [4,6, 5, 12 , 9 , 7 , 9]
n = len(nums)
print("Unsorted Array: ", nums)
quick_sort(nums, 0, n - 1  )
print("sorted Array: ", nums)




