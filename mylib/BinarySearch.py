from bisect import bisect_left, bisect_right
# bisect only work for sorted array!
array = [0,2,4,6,6,8,10]

print(bisect_left(array, 5))  # 3
print(bisect_left(array, 6))  # 3
print(bisect_left(array, 7))  # 5

print(bisect_right(array, 5)) # 3
print(bisect_right(array, 6)) # 5
print(bisect_right(array, 7)) # 5
