def binary_search(arr, target):

    n = len(arr)
    start = 0
    end = n -1

    while start <= end:
        mid = (start + end) //  2
        guess = arr[mid]

        if guess == target:
            return mid

        if guess < target:
            start = mid + 1
        else:
            end = mid - 1

    return -1

num = [2, 8 , 4 ,7 , 9 , 12 ]
target_num = 9

results = binary_search(num, target_num)
print(f"Index of target {target_num} is {results}")



