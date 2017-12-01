'''
Given a set of non-overlapping intervals, insert a new interval into the
intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their
start times.

Example 1:

Given intervals [1,3],[6,9] insert and merge [2,5] would result in [1,5],[6,9].

Example 2:

Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] would result in
[1,2],[3,10],[12,16].

This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].

Make sure the returned intervals are also sorted.
'''
# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @param new_interval, a Interval
    # @return a list of Interval
    # add/merge each interval to the new_interval depending on the overlap
    def insert(self, intervals, new_interval):
        left, right = [], []
        for interval in intervals:
            if interval.end < new_interval.start:
                left.append(interval)
            elif interval.start > new_interval.end:
                right.append(interval)
            else: # there is overlap
                lower = min(new_interval.start, interval.start)
                upper = max(new_interval.end, interval.end)
                new_interval = Interval(lower, upper)
        return left + [new_interval] + right

# test
print([(i.start, i.end) for i in Solution().insert([Interval(1,3), Interval(6,9)], Interval(2,5))])
print([(i.start, i.end) for i in Solution().insert([Interval(1,2), Interval(3,5), Interval(6,7), Interval(8,10), Interval(12,16)], Interval(4,9))])
