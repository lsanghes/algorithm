'''
Rearrange a given array so that Arr[i] becomes Arr[Arr[i]] with O(1) extra
space.

Example:

Input : [1, 0]
Return : [0, 1]
 Lets say N = size of the array. Then, following holds true :
* All elements in the array are in the range [0, N-1]
* N * N does not overflow for a signed integer
'''
class Solution:
    # @param A : list of integers
    # Modify the array A which is passed by reference.
    # You do not need to return anything in this case.

    '''
    Number encoding: (arr[arr[i]] % k) * k
    After the increment operation of first step, every element holds both old
    values and new values. Old value can be obtained by arr[i] % k and new
    value can be obtained by arr[i] // k
    k should be bigger than both numbers being encodeds
    '''
    def arrange(self, A):
        k = max(A) + 1 # k must be bigger than all vals in A for encoding
        for i in range(len(A)):
            # decode A[A[i]] as it might have been encoded already!
            new_val = A[A[i]] % k
            # encode both old vale and new value in A[i]
            A[i] = A[i] + new_val * k
        for i in range(len(A)):
            # encoded % k is the old value A[i]
            # encoded // k is the new value A[A[i]]
            A[i] = A[i] // k
        return A

    # this is O(n) space NOT O(1) space!!
    def arrange2(self, A):
        B = A[:] # A[:] or list(A) or A.copy()
        for i in range(len(A)):
            A[i] = B[B[i]]
        return A

# test
print(Solution().arrange([1,0,3,2]))
print(Solution().arrange2([1,0,3,2]))
