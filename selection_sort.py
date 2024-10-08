# selections sort is an algorithm that selects the values value in the array and moves in the front.
from typing import List


# First you go through the array and the first the lowest value.
# and then move the to front.
# and then iterate starting from the second index and then check next small value send it to the front.
# continue until all the array is sorted.


# what are the steps that are needed to implement this in a code:
# You get an unsorted array.
# An inner loop that goes through the array, finds the lowest value, brings to the front.
# This loop must loop through one less value each time runs.
# An outer loop that controls how many times the inner loop must run. For an array with n
# value, this outer loop must run `n-1` times.


# let n = 5
# we will loop 4 times which mean from 0-4:
# and perform what functions:
# get the let just say the state for the min_index =

def selection_sort(nums):
    n = len(nums)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if nums[j] < nums[min_index]:
                min_index = j
        #     swap
        nums[i], nums[min_index] = nums[min_index], nums[i]
    return nums


numbers = [7, 2, 8, 3, 9, 4, 10, 5]
selection_sort(numbers)
print(numbers)
