'''
N light bulbs are connected by a wire. Each bulb has a switch associated with
it, however due to faulty wiring, a switch also changes the state of all the
bulbs to the right of current bulb. Given an initial state of all bulbs, find
the minimum number of switches you have to press to turn on all the bulbs. You
can press the same switch multiple times.

Note : 0 represents the bulb is off and 1 represents the bulb is on.

Example:

Input : [0 1 0 1]
Return : 4

Explanation :
    press switch 0 : [1 0 1 0]
    press switch 1 : [1 1 0 1]
    press switch 2 : [1 1 1 0]
    press switch 3 : [1 1 1 1]
See Expected Output

'''
class Solution:
    # @param A : list of integers
    # @return an integer

    # O(n^2) bruteforce, flip all switches to the right of current switch
    def bulbs(self, A):
        press = 0
        for i in range(len(A)):
            if A[i] == 0:
                press += 1
                for j in range(i, len(A)):
                    A[j] = 1 - A[j] # flip all switches to the right
        return press

    # O(n) only press again if A[i] != A[i-1]
    def bulbs2(self, A):
        if not A:
            return 0
        press = 1 if A[0] == 0 else 0
        for i in range(1, len(A)):
            if A[i] != A[i-1]:
                press += 1
        return press

# test
print(Solution().bulbs([0,1,0,1]))
print(Solution().bulbs2([0,1,0,1]))
