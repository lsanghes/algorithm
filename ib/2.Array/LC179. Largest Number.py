'''
Given a list of non negative integers, arrange them such that they form the
largest number.

For example:

Given [3, 30, 34, 5, 9], the largest formed number is 9534330.

Note: The result may be very large, so you need to return a string instead of
an integer.
'''
class Solution:
    # @param A : tuple of integers
    # @return a strings
    def largestNumber(self, A):
        # 9 is largest for one digit, 99 is the largest for two digit,
        # 999 is ..etc
        # compare function based on division of largest number of its length
        compare_func = lambda x: float(x)/(10**len(str(x))-1)
        sorted_arr = sorted(A, key=compare_func, reverse=True)
        s = ''.join(map(str,sorted_arr))
        return str(int(s))

    def largestNumber2(self, A):
        import functools
        def compare_func(a, b):
            if str(a) + str(b) > str(b) + str(a):
                return 1
            elif str(a) + str(b) < str(b) + str(a):
                return -1
            return 0
        sorted_arr = sorted(A, key=functools.cmp_to_key(compare_func), reverse=True)
        s = ''.join(map(str,sorted_arr))
        return str(int(s))
# test
print(Solution().largestNumber([3, 30, 34, 5, 9]))
print(Solution().largestNumber([991, 99 ]))
print(Solution().largestNumber2([3, 30, 34, 5, 9]))
print(Solution().largestNumber2([991, 99 ]))
