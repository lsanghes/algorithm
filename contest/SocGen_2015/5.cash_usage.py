'''
Objective

The aim of this challenge is to determine which cash dispensers have delivered
the largest amount of money. For this purpose you are provided with a log file
that contains usage information.

Data Format

Input
Row 1 : an integer N between 1 and 1000 indicating the number of entries in the
log file.
Row 2 to N + 1 : a string of 8 alphanumeric characters and an integer number
between 10 and 1000 separated by a space. They represent the identifier of the
cash dispenser and the amount withdrawn.

Output
The identifiers of the 10 dispensers that have distributed the most money
ordered by descending amounts. Identifiers should be separated by a space. If
there are less than 10 dispensers in the log file, display them all. If multiple
dispensers have delivered the same amount of cash then order them by identifier
in ascending order.
'''
def solution(lines):
    from collections import Counter
    inputs = iter(lines)
    n = int(next(inputs))
    counter = Counter()
    for _ in range(n):
        identifier, val = next(inputs).split()
        counter[identifier] += int(val)

    #sort by value descending and then by identifier ascending
    top10 = sorted(counter.items(), key = lambda x:(-x[1],x[0]))[:10]
    top10keys = [k for k,v in top10]
    print(' '.join(top10keys))

# Sample Test
import os, IsoContestTest
file_path = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))
data_path = file_path + os.sep  + '5'
IsoContestTest.print_test_result(data_path, solution)
