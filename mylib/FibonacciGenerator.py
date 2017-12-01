# fib generator for the first n fib number
def fib(n):
    a, b = 1, 1
    while n:
        yield a
        a, b = b, a+b
        n -= 1

# test fib()
for num in fib(10):
    print(num)

# fib generator for infinite fib number
def fib2():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a+b

# test fib2()
n = 10
for num in fib2():
    print(num)
    n -= 1
    if not n: break
