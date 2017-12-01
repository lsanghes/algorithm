array = ['A','B','C','D','E','F','G','H','I','J']
#         0   1   2   3   4   5   6   7   8   9

n = len(array)
print(n) # 10

k = 3 # substring size of 3
print(n-k) # last stating index

for i in range(n - k + 1):
    print(array[i: i+k]) # rolling windows of k
