'''
Let's start with an easy challenge... Hundreds of visitors shop inside a
shopping mall . The aim of this challenge is to determine how many people are
present in the shopping mall at a given point in time.

Data

Input
Row 1 : an integer N between 10 and 1000 representing the number of customers
    who have entered the shopping mall during a day.
Row 2 : a time T between 00:00:00 and 23:59:59.
Rows 3 to N + 2 : two space-separated times between 00:00:00 and 23:59:59,
    representing the time at which a given customer entered the mall and the
    time at which he or she left. The second time will always be greater or
    equal to the first time.

Output
An integer representing the number of customers inside the mall at time T. If
a customer enters at time T or exits at time T it is considered to be inside
the mall at time T.
'''
def solution(lines):
    t = lines[1]
    res = 0
    for line in lines[2:]:
        start, end = line.split()
        if start <= t <= end:
            res += 1
    print(res)

# Sample Test
import os, IsoContestTest
file_path = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))
data_path = file_path + os.sep  + '1'
IsoContestTest.print_test_result(data_path, solution)
