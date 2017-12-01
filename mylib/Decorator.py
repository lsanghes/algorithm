def mod(f):
    def wrap(*args, **kwargs):
        ret = f(*args, **kwargs)
        return 100 * ret
    return wrap

@mod
def test(a):
    return a

print(test(1))
