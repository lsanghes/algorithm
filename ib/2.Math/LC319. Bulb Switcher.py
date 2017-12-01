'''
There are n bulbs that are initially off. You first turn on all the bulbs.
Then, you turn off every second bulb. On the third round, you toggle every
third bulb (turning on if it's off or turning off if it's on). For the ith
round, you toggle every i bulb. For the nth round, you only toggle the last
bulb. Find how many bulbs are on after n rounds.

Example:

Given n = 3.

At first, the three bulbs are [off, off, off].
After first round, the three bulbs are [on, on, on].
After second round, the three bulbs are [on, off, on].
After third round, the three bulbs are [on, off, off].

So you should return 1, because there is only one bulb is on.
'''
class Solution(object):
    # factors come in pair except for perfect square
    # bulbs are toggled even number(remain off) unless index is perfect square
    # find number of perfect squares <= n
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        count, i = 0, 1
        while i ** 2 <= n:
            count += 1
            i += 1
        return count

    # for all int i where 1 <= i <= sqrt(n), i^2 is a perfect square <= n
    def bulbSwitch2(self, n):
        return int(n ** 0.5)

# test
print(Solution().bulbSwitch(100))
print(Solution().bulbSwitch2(100))
