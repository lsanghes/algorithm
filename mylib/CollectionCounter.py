from collections import Counter
# ways to initalzie the Counter object
A1 = Counter('aaabbc')
A2 = Counter({'a':3, 'b':2, 'c':1})
A3 = Counter(a=3, b=2, c=1)
A4 = Counter(['a','a','a','b','b','c'])
A5 = Counter()
A5['a'] = 3
A5['b'] = 2
A5['c'] = 1
c = Counter('aaabbc')
d = Counter('bcdd')
print('A1               : {}'.format(A1))
print('A2               : {}'.format(A2))
print('A3               : {}'.format(A3))
print('A4               : {}'.format(A4))
print('A5               : {}'.format(A5))
print('c                : {}'.format(c))
print('d                : {}'.format(d))
print('c & d            : {}'.format(c & d)) # intersection:min(c[x], d[x])
print('c | d            : {}'.format(c | d)) # union:max(c[x], d[x])
# +/- operation only keeps positive count!!
print('c + d            : {}'.format(c + d)) # add two counters:c[x] + d[x]
print('c - d            : {}'.format(c - d)) # subtract:c[x]-d[x]
print('c.elements()     : {}'.format(list(c.elements())))
print('c.most_common()  : {}'.format(c.most_common()))
print('c.most_common(2) : {}'.format(c.most_common(2)))
c.subtract(d) # same as c - d but include -ve count
print('c.subtract(d);c  : {}'.format(c))
c.update(d) # same as c + d but include -ve count
print('c.update(d);c    : {}'.format(c))
e = Counter(a=-1, b=1)
print('e                : {}'.format(e)) # same as x=Counter(); x+e
print('+e               : {}'.format(+e)) # same as x=Counter(); x+e
print('-e               : {}'.format(-e)) # same as x=Counter(); x-e

# common operation
sum(c.values())                 # total of all counts
c.clear()                       # reset all counts
list(c)                         # list unique elements
set(c)                          # convert to a set
dict(c)                         # convert to a regular dictionary
c.items()                       # convert to a list of (elem, cnt) pairs
# c.most_common()[:-n-1:-1]     # n least common elements
+c                              # remove zero and negative counts
