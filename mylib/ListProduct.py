def product(nums):
    p = 1
    for n in nums:
        p *= n
    return p

def product2(nums):
    from functools import reduce
    return reduce(lambda a, b : a * b, nums)

# test
print(product([-1, 3, 100, 70, 50]))
print(product2([-1, 3, 100, 70, 50]))
