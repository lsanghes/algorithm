'''
There are len(ratings) children standing in a line. Each child is assigned a
rating value.

You are giving candies to these children subjected to the following
requirements:

- Each child must have at least one candy.
- Children with a higher rating get more candies than their neighbors.

What is the minimum candies you must give?
'''
class Solution:
    # O(N) two passes, one forward and one backward
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        if not ratings:
            return 0
        candies = [1] * len(ratings)
        for i in range(1, len(ratings)): # 1st pass forward
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1
        for i in reversed(range(1, len(ratings))): # 2nd pass backward
            if ratings[i-1] > ratings[i]:
                candies[i-1] = max(candies[i-1], candies[i] + 1)
        return sum(candies)

# test
# rating:   1 2 3 1 3 2 1 4
# inital:   1 1 1 1 1 1 1 1 = 8
# forward:  1 2 3 1 2 1 1 2 = 13
# backward: 1 2 3 1 3 2 1 2 = 15
print(Solution().candy([1,2,3,1,3,2,1,4]))
print(Solution().candy([1,2]))
