'''
O(log(m+n))
# find first i elements from shorter array, and first j elements from longer
array where j = k - i
'''
def findkth(A, B, k):
    m, n = len(A), len(B)
    if m > n:
        return findkth(B, A, k)
    if m == 0:
        return B[k-1] # kth element of array B
    if k == 1:
        return min(A[0],B[0])
    i = min(k//2, m) # number of elements in shorter array
    j = k - i # number of elements in longer array
    if A[i-1] < B[j-1]: # all elements in A[:i] are smaller than kth element
        return findkth(A[i:], B, k-i) # discard A[:i]
    else: # all elements in B[:j] are smaller or eqaul than kth element
          # if there is equal case, the same number is still in array A
        return findkth(A, B[j:], k-j) # discard B[:j]

'''
O(log(min(A,B)))
find i, j such that i + j = k - 1 and first i elements from A and first j
elements from B are in kth array, then min(A[i], B[j]) should be kth element
'''
def findkth2(A, B, k):
    m, n = len(A), len(B)
    if m > n:
        return findkth(B, A, k)
    lo, hi = max(0, k-n-1), min(m, k)
    while lo <= hi:
        i = (lo + hi) // 2
        j = k - i - 1
        # j and i condition ensure condition checks are not out of index
        if j > 0 and i < m and A[i] < B[j-1]: # i is too small
            lo = i + 1
        elif i > 0 and j < n and A[i-1] > B[j]: # i is too big
            hi = i - 1
        else: # A[i] >= B[j-1] and B[j] >= A[i-1] or i,j are out of index
            return min(A[i:i+1] + B[j:j+1]) # use slicing to avoid out-of-range

# test
A = [4, 5, 6, 7, 8, 9, 10]
B = [1, 2, 3, 11, 12, 13, 14, 15]
for i in range(1, max(A+B)+1):
    print(findkth(A, B, i))
    print(findkth2(A, B, i))
