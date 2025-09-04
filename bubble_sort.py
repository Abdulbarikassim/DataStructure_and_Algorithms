# Bubble bubble_sort - This is an algorithms that bubble_sort items from the lowest to highest in a list.

# ascending order of list.
# add edge cases for the code:
# what happens if an empty array is passed.
# if only the array has one value.
# and if everything in array is the same.
# This code now solve both positive and negative integers in a list.

# def bubble_sort(nums):
#     try:
#         if len(nums) <= 0 or len(nums) < 1:
#             raise ValueError("Number should be more than two for comparison")
#         elif all(x == nums[0] for x in nums):
#             raise ValueError(f"Cannot bubble_sort if all the values of the array are equal")
#         # outer loop.
#         for i in range(len(nums) - 1):
#             swapped = False
#             for j in range(len(nums) - i - 1):
#                 if nums[j] > nums[j + 1]:
#                     temp = nums[j]
#                     nums[j] = nums[j + 1]
#                     nums[j + 1] = temp
#                     swapped = True
#
#             if not swapped:
#                 break
#     except Exception as e:
#         print(e)
#

def bubble_sort(arr):
    swapped  = True
    end = len(arr)

    while swapped:
        swapped =  False
        for i in range(1, end):
            if arr[i-1] > arr[i]:
                arr[i-1], arr[i] = arr[i] , arr[i-1]

                swapped = True
        end -= 1
    return arr

numbers = [4, 2, 7, 5, 12, 10, 8, 6]

bubble_sort(numbers)
print(numbers)
