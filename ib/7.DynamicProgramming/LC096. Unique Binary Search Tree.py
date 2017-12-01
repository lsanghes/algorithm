'''
Given n, how many structurally unique BST's (binary search trees) that store
values 1...n?

For example,
Given n = 3, there are a total of 5 unique BST's.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
'''
class Solution:
    '''
    To build a tree contains {1,2,3,4,5}. First we pick 1 as root, for the
    left sub tree, there are none; for the right sub tree, we need count how
    many possible trees are there constructed from {2,3,4,5}, apparently
    that's the same number as {1,2,3,4}. So the total number of trees
    under "1" picked as root is dp[0]*dp[4] = 14. (dp[0]=1 for empty tree).
    Similarly, root 2 has dp[1]*dp[3] = 5 trees. root 3 has dp[2]*dp[2] = 4,
    root 4 has dp[3]*dp[1]= 5 and root 5 has dp[4]*dp[0] = 14.
    Finally sum up all
    '''
    # bruteforce resursive
    def numTrees(self, n):
        if not n:
            return 1
        return sum([self.numTrees(i) * self.numTrees(n-1-i) for i in range(n)])

    # dp buttom up
    # F(n) = F(0) * F(n-1) + F(1) * F(n-2) + F(2) * F(n-3) + ... + F(n-1) * F(0)
    # F(5) = F(0) * F(4) + F(1) * F(3) + F(2) * F(2) + F(3) * F(1) + F(4) * F(0)
    # interatively calculate result for n = 1,2,3,4,5
    def numTrees2(self, n):
        if not n:
            return 1
        dp = [0] * (n + 1)
        dp[0], dp[1] = 1, 1
        for i in range(2, n+1): # build F(n) up to i
            for j in range(1, i+1):
                dp[i] += dp[j-1] * dp[i-j] # actual F(n) for each i
        return dp[n]

# test
for n in range(0, 6):
    print(Solution().numTrees(n))
    print(Solution().numTrees2(n))
