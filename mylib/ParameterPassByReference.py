# primiative local variable CANNOT be modified by reference
x, y = 0, 0
def f1():
    try:
        x += 1 # UnboundLocalError
    except Exception as e:
        print('{}: {}'.format(type(e), e))
f1()

# function parameter n is just a new copy of x
x = 0
print("Value of x before f2(x): {}".format(x))
def f2(n):
    n += 1
f2(x)
print("Value of x after f2(x) : {}".format(x))

# access by reference using non-primative
x = [0]
print("Value of x before f3(): {}".format(x[0]))
def f3():
    x[0] += 1
f3()
print("Value of x after f3() : {}".format(x[0]))

# access by reference using class property
class Class:
    def __init__(self):
        self.x = 0
    def f4(self):
        self.x += 1
c = Class()
print("Value of x before f4(): {}".format(c.x))
c.f4()
print("Value of x after f4() : {}".format(c.x))
