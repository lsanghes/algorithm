def flatten_list(lis):
    """Given a list, possibly nested to any level, return it flattened."""
    new_lis = []
    for item in lis:
        if type(item) == type([]):
            new_lis.extend(flatten(item))
        else:
            new_lis.append(item)
    return new_lis

def flatten(x):
    return [y for l in x for y in flatten(l)] if type(x)==type([]) else [x]

# test
a = [1, 2, [3, 4], [[5, 6], [7, 8]]]
print(flatten(a))
print(flatten_list(a))

# a must contain non-nested list! bad performance
a = [[3, 4], [5, 6], [7, 8], []]
print(sum(a, []))
