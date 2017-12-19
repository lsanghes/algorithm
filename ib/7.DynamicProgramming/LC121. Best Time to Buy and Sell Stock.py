'''
Say you have an array for which the ith element is the price of a given stock
on day i.

If you were only permitted to complete at most one transaction (ie, buy one and
sell one share of the stock), design an algorithm to find the maximum profit.

Example 1:
Input: [7, 1, 5, 3, 6, 4]
Output: 5

max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger
than buying price)

Example 2:
Input: [7, 6, 4, 3, 1]
Output: 0

In this case, no transaction is done, i.e. max profit = 0.
Subscribe to see which companies asked this question
'''
class Solution:
    # https://en.wikipedia.org/wiki/Maximum_subarray_problem
    # DP - Kadane's algorithm for Maximum Subarray
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        local_max = global_max = 0
        for i in range(1, len(prices)):
            x = prices[i] - prices[i-1]
            local_max = max(0, local_max + x)
            global_max = max(global_max, local_max)
        return global_max

    # Finite State Machine - 3 states 5 transitions
    # beforebuy --- (rest) ---> beforebuy
    # beforebuy --- (buy ) ---> bought
    # bought    --- (rest) ---> bought
    # bought    --- (sell) ---> sold
    # sold      --- (rest) ---> sold
    def maxProfit2(self, prices):
        if not prices:
            return 0
        buy, sell = prices[0], 0 # initial state
        for p in prices[1:]:
            # states can be updated separately due to sequential dependencies
            buy = min(p, buy)
            sell = max(p - buy, sell)
        return sell

# test
print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
print(Solution().maxProfit([7, 6, 4, 3, 1]))
print(Solution().maxProfit2([7, 1, 5, 3, 6, 4]))
print(Solution().maxProfit2([7, 6, 4, 3, 1]))
