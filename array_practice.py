# create an Algorithms to check give the lowest value in an array.
my_array = [12,4,43,8,10,5,2]
min_value =  my_array[0]


for lowest_value in my_array:
    if lowest_value < min_value:
        min_value = lowest_value

print(f"Lowest Value in the array : {min_value}")





