from time import time
import random as rand

start = time()

def partition(left : int, right : int, num_arr : "list[int]") -> int:

    pivot, point = num_arr[right], left

    for i in range(left, right):

        if num_arr[i] <= pivot:
            num_arr[i], num_arr[point] = num_arr[point], num_arr[i]
            point += 1

    num_arr[point], num_arr[right] = num_arr[right], num_arr[point]
    return point


def quicksort(left : int, right : int, num_arr : "list[int]") -> "list[int]":

    if len(num_arr) == 1:  
        return num_arr

    if left < right:
        temp_arr = partition(left, right, num_arr)
        quicksort(left, temp_arr-1, num_arr)
        quicksort(temp_arr+1, right, num_arr)

    return num_arr
 
#Problem A
array = [10, 80, 3, 19, 14, 7, 5, 12]
quicksort(0, len(array) - 1, array)
print(f'The sorted array is: {array}, and was executed in {time() - start} seconds')

#Problem B
b_array = []

for i in range(0,100):
    b_array.append(rand.randint(0 , 100))

quicksort(0, len(b_array) - 1, b_array)
print(f'The sorted array is: {b_array}, and was executed in {time() - start} seconds')

# Problem C
c_array = []

for i in range(0,1000):
    c_array.append(rand.randint(0 , 1000))

quicksort(0, len(c_array) - 1, c_array)
print(f'The sorted array is: {c_array}, and was executed in {time() - start} seconds')