# quick sort, inplace O(nlogn) with randomization
def quicksort(A):
    import random
    def partition(A, lo, hi):
        # maintain two pointers:
        # one for the divider position the other one for curr items in the list
        pivot_ix = hi # the last element will be pivot
        divider_ix = lo # cur divider is the first item
        for i in range(lo, hi):
            if A[i] < A[pivot_ix]:
                A[i], A[divider_ix] = A[divider_ix], A[i]
                divider_ix += 1
        # after for loop, all elements in A[:divider_ix] is < A[pivot_ix]
        # ie. pivot should be in the position of divider_ix
        A[pivot_ix], A[divider_ix] = A[divider_ix], A[pivot_ix]
        # everything on the left of pivot is smaller than pivot
        # everything on the right of pivot is bigger or equal than pivot
        return divider_ix
    def sort(A, lo, hi):
        if lo < hi:
            pivot = partition(A, lo, hi)
            sort(A, lo, pivot-1)
            sort(A, pivot+1, hi)
    random.shuffle(A) # random shuffle ensure O(nlogn) on average
    sort(A, 0, len(A)-1)
    return A

# test
array = list(reversed(range(20)))
print(array)
quicksort(array)
print(array)
