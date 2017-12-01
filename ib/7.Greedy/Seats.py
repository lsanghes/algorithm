'''
There is a row of seats. Assume that it contains N seats adjacent to each
other. There is a group of people who are already seated in that row randomly.
i.e. some are sitting together & some are scattered.

An occupied seat is marked with a character 'x' and an unoccupied seat is
marked with a dot ('.')

Now your target is to make the whole group sit together i.e. next to each
other, without having any vacant seat between them in such a way that the total
number of hops or jumps to move them should be minimum.

Return minimum value % MOD where MOD = 10000003

Example

Here is the row having 15 seats represented by the String (0, 1, 2, 3, ... , 14)

              . . . . x . . x x . . . x . .

Now to make them sit together one of approaches is -
                  . . . . . . x x x x . . . . .

Following are the steps to achieve this -
1 - Move the person sitting at 4th index to 6th index -
    Number of jumps by him =   (6 - 4) = 2

2 - Bring the person sitting at 12th index to 9th index -
    Number of jumps by him = (12 - 9) = 3

So now the total number of jumps made =
    ( 2 + 3 ) % MOD =
    5 which is the minimum possible jumps to make them seat together.

There are also other ways to make them sit together but the number of jumps
will exceed 5 and that will not be minimum.

For example bring them all towards the starting of the row i.e. start placing
them from index 0. In that case the total number of jumps will be
    ( 4 + 6 + 6 + 9 )%MOD
    = 25 which is very costly and not an optimized way to do this movement

'''
class Solution:
    # TLE - O(n^2) brutefore moving window of size = No. of people
    # calculate total hops to move all people to seats in cur window
    # ie. moving windows {[0:p],[1:p+1].. [n-p:n]}
    #   .x..xx   <-- original seating
    #   xxx... 7 hops to move 3 people to window [0, 2]
    #   .xxx.. 4 hops to move 3 people to window [1, 3]
    #   ..xxx. 3 hops to move 3 people to window [2, 4]
    #   ...xxx 2 hops to move 3 people to window [3, 5]
    def seats(self, A):
        people = len([a for a in A if a == 'x'])
        min_hops = float('inf')
        for j in range(len(A) - people + 1):
            hops = 0
            k = j
            for i, a in enumerate(A):
                if a == 'x': # occupied seat by someone
                    hops += abs(i - k) # move that people to cur seat
                    k += 1 # move to next seat
                if k - j > people:
                    break # all seats in cur window are filled, no more people
            min_hops = min(min_hops, hops)
        return min_hops % 10000003

    # O(n)
    def seats2(self, A):
        # generate seating groups without all empty seat in between
        groups = []
        j = 0
        while j < len(A):
            if A[j] == '.':
                # keep skipping empty seat till an occupied seat
                j += 1
                continue
            k = j # both j, k is at start of cur group
            while k < len(A) and A[k] == 'x':
                k += 1 # move k to the end of the group
            groups.append([j, k-1])
            j = k # skip to end of cur group for the new group
        # now groups contain all seating groups
        # start from outside, and move the smaller group to the center
        hops = 0
        j, k = 0, len(groups) - 1
        while j < k:
            left_len = groups[j][1] - groups[j][0] + 1
            right_len = groups[k][1] - groups[k][0] + 1
            if left_len < right_len:
                # merge left most group into inner group
                hops += left_len * (groups[j+1][0] - groups[j][1] - 1)
                groups[j+1][0] -= left_len # update inner group range
                j += 1
            else:
                # merge right most group into inner group
                hops += right_len * (groups[k][0] - groups[k-1][1] - 1)
                groups[k-1][1] += right_len # update inner group range
                k -= 1
        return hops % 10000003

# test
print(Solution().seats('.x..xx'))
print(Solution().seats('....x..xx...x..'))
print(Solution().seats('xx.....xx.x..xxxx..xxxx.xx..xx..x.xxxx'))
print(Solution().seats2('.x..xx'))
print(Solution().seats2('....x..xx...x..'))
print(Solution().seats2('xx.....xx.x..xxxx..xxxx.xx..xx..x.xxxx'))
