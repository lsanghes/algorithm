nested = [[1, 2, 3, 4], [5, 6, 7, 8]]

print([[i for i in r] for r in nested])
# [[1, 2, 3, 4], [5, 6, 7, 8]]

print([i for r in nested for i in r])
# [1, 2, 3, 4, 5, 6, 7, 8]

print([[i] for r in nested for i in r])
# [[1], [2], [3], [4], [5], [6], [7], [8]]
