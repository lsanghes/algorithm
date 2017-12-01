'''
Given an array with non negative numbers, divide the array into two parts such
that the average of both the parts is equal. Return both parts (If exist).
If there is no solution. return an empty list.

Example:

Input:
[1 7 15 29 11 9]

Output:
[9 15] [1 7 11 29]

The average of part is (15+9)/2 = 12,
average of second part elements is (1 + 7 + 11 + 29) / 4 = 12

 NOTE 1: If a solution exists, you should return a list of exactly 2 lists of
 integers A and B which follow the following condition :
* numElements in A <= numElements in B
* If numElements in A = numElements in B, then A is lexicographically smaller
than B ( https://en.wikipedia.org/wiki/Lexicographical_order )

 NOTE 2: If multiple solutions exist, return the solution where length(A) is
 minimum. If there is still a tie, return the one where A is lexicographically
 smallest.

 NOTE 3: Array will contain only non negative numbers.
'''
class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def avgset(self, A):
        # find n numbers from array A starting from index i
        # such that sum of these n numbers is target_sum
        # store the result in dp
        def is_valid(i, n, target_sum, dp):
            # target might not be exactly zero due to division
            key = (i, n, target_sum)
            if key in dp: # known result
                return dp[key]
            if n == 0 and abs(target_sum) < 1e-10: # base case1
                return True
            if i > len(A) - 1 or n < 0: # base case 2
                return False
            # curr item is part of the result
            cond1 = is_valid(i+1, n-1, target_sum-A[i], dp)
            # curr item is not part of the result
            cond2 = is_valid(i+1, n, target_sum, dp)
            dp[key] = cond1 or cond2
            return dp[key]

        A.sort() # ensure lexicographical order
        avg = sum(A) / float(len(A))
        # dp = {} # MLE if dp is defined ouside the loop but it's not wrong!
        for n in range(1, len(A)//2 + 1):
            # one of the two arrays must be <= half len if answer exist
            # n is number of items in the first array
            dp = {} # refresh dp for each loop to save memory
            target_sum = n * avg
            if is_valid(0, n, target_sum, dp):
                # found a valid result, n element should be in first array
                # now we need to decide which elements go to first array
                first, second = [], []
                for j in range(len(A)):
                    if is_valid(j+1, n-1, target_sum-A[j], dp):
                         # j should be in 1st array since we found n-1 elements
                         # such that total sum including j = target_sum
                        first.append(A[j])
                        n -= 1
                        target_sum -= A[j]
                    else: # j should be 2nd array
                        second.append(A[j])
                # print(len(dp)) # check how many results are cached
                return [first, second] # return the first result found
        return []

# test
print(Solution().avgset([1,2,3,4,5]))
print(Solution().avgset([16,42,18,48,26,45,46,26,25,7,7,48,30,10,10,3,1,11,33,
                         14,21,15]))
