'''
Say you have an array for which the ith element is the price of a given stock
on day i.

Design an algorithm to find the maximum profit. You may complete as many
transactions as you like (ie, buy one and sell one share of the stock multiple
times) with the following restrictions:

- You may not engage in multiple transactions at the same time (ie, you must
sell the stock before you buy again).
- After you sell your stock, you cannot buy stock on next day. (ie, cooldown
1 day)

Example:

prices = [1, 2, 3, 0, 2]
maxProfit = 3
transactions = [buy, sell, cooldown, buy, sell]
'''
class Solution:
    # Finite State Machine - 3 states 5 transitions
    # bought --- (rest) ---> bought
    # bought --- (sell) ---> sold
    # cooled --- (rest) ---> cooled
    # cooled --- (buy ) ---> bought
    # sold   --- (rest) ---> cooled
    def maxProfit(self, prices):
        if len(prices) < 2:
            return 0
        bought, sold, cooled = -prices[0], 0, 0
        for p in prices[1:]:
            # states must be updated at the same time due to inter-dependecy
            bought,sold,cooled = max(bought,cooled-p),bought+p,max(cooled,sold)
        return max(cooled, sold)

# test
print(Solution().maxProfit([1, 2, 3, 0, 2]))
