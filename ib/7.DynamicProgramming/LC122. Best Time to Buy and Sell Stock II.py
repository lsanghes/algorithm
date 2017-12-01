'''
Say you have an array for which the ith element is the price of a given stock
on day i.

Design an algorithm to find the maximum profit. You may complete as many
transactions as you like (ie, buy one and sell one share of the stock multiple
times). However, you may not engage in multiple transactions at the same time
(ie, you must sell the stock before you buy again).
'''
class Solution:
    # dp
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        res = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                res += prices[i] - prices[i-1]
        return res

    # nice use of sum
    def maxProfit2(self, prices):
        return sum(max(0, prices[i]-prices[i-1]) for i in range(1, len(prices)))

    # nice way to zip A[i] and A[i+1]
    def maxProfit3(self, prices):
        return sum((y-x for x, y in zip(prices[:-1], prices[1:]) if y > x ))

    # Finite State Machine - 3 states 6 transitions
    # beforebuy --- (rest) ---> beforebuy
    # beforebuy --- (buy ) ---> bought
    # bought    --- (rest) ---> bought
    # bought    --- (sell) ---> sold
    # sold      --- (rest) ---> sold
    # sold      --- (buy)  ---> bought
    def maxProfit4(self, prices):
        if len(prices) < 2:
            return 0
        buy, sell = -prices[0], 0 # initial state
        for p in prices[1:]:
            # states must be updated at the same time due to inter-dependecy
            buy, sell = max(buy, sell-p), max(sell, buy+p)
        return sell

# test
print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
print(Solution().maxProfit2([7, 1, 5, 3, 6, 4]))
print(Solution().maxProfit3([7, 1, 5, 3, 6, 4]))
print(Solution().maxProfit4([7, 1, 5, 3, 6, 4]))
