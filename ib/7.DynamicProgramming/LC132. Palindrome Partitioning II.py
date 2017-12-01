'''
Given a string s, partition s such that every substring of the partition is a
palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

Example :
Given
s = "aab",
Return 1 since the palindrome partitioning ["aa","b"] could be produced using
1 cut.
'''
class Solution:
    # DP - O(N^3) because of [::-1]
    # s  :  x y z abba  c
    # cut:  0 1 2 3  3  4
    #             j  k  min(7,4)
    # if s[j:k+1] is palindrome, then cut[k+1] = cut[j] + 1
    #                            i.e. cut[k] = cut[j-1] + 1
    def minCut(self, s):
        n = len(s)
        cut = [i for i in range(n)] # maximum cut at each index
        for j in range(n):
            for k in range(j, n):
                pre = s[j:k+1]
                if pre == pre[::-1]:
                    cut[k] = min(cut[j-1]+1, cut[k]) if j else 0
        return cut[-1]

    # O(N^2) - update cut for every possible palindrome found!
    # time complexitiy reduce because not using [::-1]
    def minCut2(self, s):
        n = len(s)
        cut = [i for i in range(n)] # maximum cut at each index
        for i in range(n):
            # [j,k] are the start and end of palindrome
            j, k = i, i # palindrome of odd number
            while j>=0 and k<n and s[j] == s[k]:
                cut[k] = min(cut[j-1]+1, cut[k]) if j else 0
                j, k = j-1, k+1
            j, k = i, i+1 # palindrome of even number
            while j>=0 and k<n and s[j] == s[k]:
                cut[k] = min(cut[j-1]+1, cut[k]) if j else 0
                j, k = j-1, k+1
        return cut[-1]

# test
print(Solution().minCut("ccaacabacb"))
print(Solution().minCut2("ccaacabacb"))
print(Solution().minCut3("ccaacabacb"))
