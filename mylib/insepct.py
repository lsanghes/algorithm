import tf_utils
from inspect import getmembers, isfunction, getsource
for o in getmembers(tf_utils):
    if isfunction(o[1]):
        print(getsource(o[1]))

