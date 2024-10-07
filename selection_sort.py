# selections sort is an algorithm that selects the values value in the array and moves in the front.
from typing import List

# First you go through the array and the first the lowest value.
# and then move the to front.
# and then iterate starting from the second index and then check then next small value send it to the front.
# continue until all the array is sorted.

# Implementing the selection sort:
# outer loop checks how many times the inner loop runs.
# inner loop goes through everything and then  moves the smallest value to the front.

nums = [3, 7, 9, 11, 12]

n = len(nums)


