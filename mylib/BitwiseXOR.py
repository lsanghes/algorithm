'''
x^y - bitwise exclusive or:
    return 1 only if one of x, y is 1.
    XOR with 1 can be used to flip the bit

n^0 = n             XORing with 0 returns the same number
n^1 = ~n            XORing with 1 returns negation of the bit
n^n = 0             XORing with itself returns 0
n^m = m^n           XOR is commutative
(n^m)^p = n^(m^p)   XOR is associative
'''
