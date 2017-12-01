d = {1:30, 2:20, 3:20}

from collections import OrderedDict
# desc by value and then desc by key
print(OrderedDict(sorted(d.items(), key=lambda x: (-x[1], -x[0]))))
# asc by key and then asc by value
print(OrderedDict(sorted(d.items(), key=lambda x: ( x[0],  x[1]))))
