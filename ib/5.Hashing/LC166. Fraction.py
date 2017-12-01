'''
Given two integers representing the numerator and denominator of a fraction,
return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

For example,

Given numerator = 1, denominator = 2, return "0.5".
Given numerator = 2, denominator = 1, return "2".
Given numerator = 2, denominator = 3, return "0.(6)".
'''
class Solution:
    def fractionToDecimal(self, numerator, denominator):
        head = '-' if numerator * denominator < 0 else ''
        numerator, denominator = abs(numerator), abs(denominator)
        whole, r = divmod(numerator, denominator)
        head += str(whole)
        seen, tail = {}, ''
        if r: # process the decimal part
            head += '.'
            dec_ix = 0
            while r:
                if r not in seen:
                    seen[r] = dec_ix
                    dec_ix += 1
                    # we can also use len(tail) to track dec_ix
                    q, r = divmod(r * 10, denominator)
                    tail += str(q)
                else:
                    i = seen[r]
                    tail = tail[:i] + '(' + tail[i:] + ')'
                    break
        return head + tail

# test
print(Solution().fractionToDecimal(1, 2))
print(Solution().fractionToDecimal(2, 1))
print(Solution().fractionToDecimal(2, 3))
print(Solution().fractionToDecimal(10, 8))
print(Solution().fractionToDecimal(1, -6))
print(Solution().fractionToDecimal(100, 11))
