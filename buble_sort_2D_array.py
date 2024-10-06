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

