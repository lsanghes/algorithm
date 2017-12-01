# (n-1)//2  return mid index for odd array
# (n-1)//2  return left mid index for even array
# (n+1)//2  return right mid index for even array
def find_median(array):
    array.sort() # array must be sorted
    n = len(array)
    if n % 2 == 0: # even array
        mid_ix_left  = (n-1) // 2
        mid_ix_right = (n+1) // 2
        return (array[mid_ix_left] + array[mid_ix_right]) / 2.0
    else: # odd array
        mid_ix = (n-1) // 2
        return array[mid_ix]

# test
even_array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] # n=10
odd_array  = [0, 1, 2, 3, 4, 5, 6, 7, 8]    # n=9
print(find_median(even_array))
print(find_median(odd_array))
