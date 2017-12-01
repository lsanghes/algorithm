m = [[i*j for i in range(2,12)] for j in range(25,35)]

# import pandas as pd
# print(pd.DataFrame(m))

def print_2d(matrix):
    if not matrix or not matrix[0]:
        print("Empty\n")
        return
    #important make new copy!
    grid = [[str(i) for i in row] for row in matrix]
    grid.insert(0, list(range(len(grid[0]))))
    for r in range(len(grid)):
        grid[r].insert(0, r-1)
    grid[0][0] = ''
    s = [[str(i) for i in row] for row in grid]
    lengths = [max(map(len, col))+2 for col in zip(*s)]
    fmt = ''.join('{{:>{}}}'.format(x) for x in lengths)
    table = [fmt.format(*row) for row in s]
    print('\n'.join(table))

# test
print_2d(m)
