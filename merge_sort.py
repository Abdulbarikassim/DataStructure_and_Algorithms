"""
merge sort: Its a popular sorting algorithms  known for it efficiency and stability. It uses the divide and conquer approach. It works by constant dividing the input array into two, recursively sorting them and finally merging both together.

Time complexity:
- worst time complexity: O(n log n )
- best time complexity: O(n log n )
- average time complexity: O(n log n )

Pros:

Fast: Merge sort is much faster than bubble sort. O(n*log(n)) instead of O(n^2).
Stable: Merge sort is a stable sort which means that values with duplicate keys in the original list will be in the same order in the sorted list.

Cons:
    Memory usage: Most sorting algorithms can be performed using a single copy of the original array. Merge sort requires extra subarrays in memory.
    Recursive: Merge sort requires many recursive function calls, and in many languages (like Python), this can incur a performance penalty.
"""

def merge_sort(nums):
    if len(nums) < 2:
        return nums

    mid = len(nums) // 2
    first_half = nums[:mid]
    second_half = nums[mid:]

    first = merge_sort(first_half)
    second = merge_sort(second_half)

    return merge(first, second)



def merge(first, second):
    final = []
    i = 0
    j = 0
    while i < len(first) and j < len(second):
        if first[i] <= second[j]:
            final.append(first[i])
            i += 1
        else:
            final.append(second[j])
            j += 1
    final.extend(first[i:])
    final.extend(second[j:])
    return final


nums = [4, 1, 3, 2]
sorted_nums = merge_sort(nums)
print("Original:", nums)
print("Sorted:", sorted_nums)










