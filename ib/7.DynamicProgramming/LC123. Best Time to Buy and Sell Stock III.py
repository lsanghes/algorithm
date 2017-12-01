'''
Say you have an array for which the ith element is the price of a given stock
on day i.

Design an algorithm to find the maximum profit. You may complete at most two
transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell
the stock before you buy again).

Example :

Input : [1 2 1 2]
Output : 2

Explanation :
  Day 1 : Buy
  Day 2 : Sell
  Day 3 : Buy
  Day 4 : Sell
'''
class Solution:
    # Finite State Machine - 5 states 9 transitions
    # beforebuy --- (rest) ---> beforebuy
    # beforebuy --- (buy ) ---> b1
    # b1        --- (rest) ---> b1
    # b1        --- (sell) ---> s1
    # s1        --- (rest) ---> s1
    # s1        --- (buy)  ---> b2
    # b2        --- (rest) ---> b2
    # b2        --- (sell) ---> s2
    # s2        --- (rest) ---> s2
    def maxProfit(self, prices):
        if len(prices) < 2:
            return 0
        b1, s1, b2, s2 = -prices[0], 0, -prices[0], 0
        for p in prices[1:]:
            # states can be updated separately due to sequential dependencies
            b1 = max(b1, -p)
            s1 = max(s1, b1+p)
            b2 = max(b2, s1-p)
            s2 = max(s2, b2+p)
        return s2

# test
print(Solution().maxProfit([1,2,1,2]))
print(Solution().maxProfit([7,1,5,3,6,4]))
print(Solution().maxProfit([1,2]))
