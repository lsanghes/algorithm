'''
Please Note:

Another question which belongs to the category of questions which are
intentionally stated vaguely.
Expectation is that you will ask for correct clarification or you will state
your assumptions before you start coding.

Given an integer, convert it to a roman numeral, and return a string
corresponding to its roman numeral version

Input is guaranteed to be within the range from 1 to 3999.

Example :

Input : 5
Return : "V"

Input : 14
Return : "XIV"
 Note : This question has a lot of scope of clarification from the interviewer.
 Please take a moment to think of all the needed clarifications and see the
 expected response using “See Expected Output” For the purpose of this question,
 https://projecteuler.net/about=roman_numerals has very detailed explanations.
'''
class Solution:
    # @param A : integer
    # @return a strings
    '''
    I = 1
    V = 5
    X = 10
    L = 50
    C = 100
    D = 500
    M = 1000
    D, L, and V can each only appear once.
    The "descending size" rule was introduced to allow the use of subtractive
    combinations
    four can be written IV because it is one before five.
    '''
    def intToRoman(self, A):
        roman = {'M':1000,'CM':900,'D':500,'CD':400,'C':100,'XC':90,'L':50,
                 'XL':40,'X':10,'IX':9,'V':5,'IV':4,'I':1}
        res = ''
        remainder = A
        for k, v in sorted(roman.items(), key=lambda x: -x[1]): # sort by v desc
            q, remainder = divmod(remainder, v)
            res += k * q
        return res

# test
print(Solution().intToRoman(14))
print(Solution().intToRoman(990))
