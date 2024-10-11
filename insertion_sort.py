# Insertion sort - This is a method that uses one part as the sorted and the other part as the unsorted.
# steps:
# 1. Use the first value as the sorted
# 2. Move the rest of the unsorted values to the sorted part checking and then putting them in the correct position.
# 3. Repeat that again and again until all the array is sorted.
# so in the inner loop what you have to make sure is the start of the loop, stop and direction or step.
# for insertion for j in range(i-1,-1,-1) we start just before the i
# we stop at the last value, then  we move in reverse direction meaning from right to left.


def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        insert_index = i
        value = arr[i]
        for j in range(i-1, -1, -1):
            if arr[j] > value:
                arr[j+1] = arr[j]
                insert_index = j
            else:
                break
        arr[insert_index] = value


numbers = [9, 2, 4, 3, 12, 10, 8, 7, 14, 11]
insertion_sort(numbers)
print(numbers)






