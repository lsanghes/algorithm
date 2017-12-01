'''
Say you have an array for which the ith element is the price of a given stock
on day i.

Design an algorithm to find the maximum profit. You may complete at most k
transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must
sell the stock before you buy again).
'''
class Solution:
    # dp - O(kn)
    # still an FSM solution similar to lc123
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if k < 1 or len(prices) < 2:
            return 0
        # two transaction within same day does not change max profit!
        # therefore we need at most n//2 transaction to reach max profit when
        # i.e. prices = [lo, hi, lo, hi, ... lo,hi]
        # therefore if k >= len//2 then then it's the same as unlimited b/s
        # without this special handling lc get memory error
        if k >= len(prices) // 2:
            return sum(i-j for i,j in zip(prices[1:], prices[:-1]) if i>j)
        # same idea as lc123 for at most 2 transactions
        buys = [-prices[0]] * k
        sells = [0] * k
        for p in prices[1:]:
            for i in range(k):
                buys[i] = max(buys[i], sells[i-1]-p if i>0 else -p)
                sells[i] = max(sells[i], buys[i]+p)
        return sells[-1]

# test
print(Solution().maxProfit(2, [1,2,3,4,5,3,7,2,4])) #8
print(Solution().maxProfit(3, [1,2,3,4,5,3,7,2,4])) #10
print(Solution().maxProfit(2, [1,2,1,2])) #2
