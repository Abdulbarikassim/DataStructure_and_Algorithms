# Bubble sort - This is an algorithms that sort items from the lowest to highest in a list.

# ascending order of list.
# add edge cases for the code:
# what happens if an empty array is passed.
# if only the array has one value.
# and if everything in array is the same.
# This code now solve both positive and negative integers in a list.

# def sort(nums):
#     try:
#         if len(nums) <= 0 or len(nums) < 1:
#             raise ValueError("Number should be more than two for comparison")
#         elif all(x == nums[0] for x in nums):
#             raise ValueError(f"Cannot sort if all the values of the array are equal")
#         # outer loop.
#         for i in range(len(nums)-1):
#             swapped = False
#             for j in range(len(nums)-i-1):
#                 if nums[j] > nums[j+1]:
#                     temp = nums[j]
#                     nums[j] = nums[j+1]
#                     nums[j + 1] = temp
#                     swapped = True
#
#             if not swapped:
#                 break
#     except Exception as e:
#         print(e)
#
#
# numbers = [2,2,2,2,2]
#
#
# sort(numbers)
# # print(numbers)

# solve for a 2D array.

def sort(nums):
    for row in nums:
        for i in range(len(nums) - 1):
            swapped = False
            for j in range(len(nums) - i - 1):
                if row[j] > row[j + 1]:
                    temp = row[j]
                    row[j] = row[j + 1]
                    row[j + 1] = temp
                    swapped = True
            if not swapped:
                break


arr = [
    [9, 3, 1],
    [4, 7, 2],
    [8, 5, 6]
]

sort(arr)
print(arr)

