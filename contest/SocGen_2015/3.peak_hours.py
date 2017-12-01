'''
In this challenge, you need to determine the time at which the most employees
are working simultaneously in the building.

Data format

Input
Row 1: an integer N representing the total number of people that enter the
building over one day.
Row 2 to N + 1: 2 integers between 0 and 24, separated by a space, representing
the hours of arrival and departure of every employee.

To simplify the challenge, the first integer on each row will be strictly
smaller than the second (e.g., no employee stays overnight, and every employee
stays at least one hour). Please note that if a person is working from 8 o'clock
to 16 o'clock, it means that he or she is not working at 16 o'clock.

Output
An integer between 0 and 24 representing the time at which most people are
working inside the building. If there are multiple hours where the maximum is
reached display all of them sorted ascendingly and separated by spaces.
'''
def solution(lines):
    from collections import Counter
    inputs = iter(lines)
    counter = Counter()
    n = int(next(inputs))
    for _ in range(n):
    	arrival, departure = next(inputs).split()
    	for i in range(int(arrival), int(departure)):
    		counter[i] += 1
    max_ppl = max(counter.values())
    max_hrs = [str(k) for k,v in sorted(counter.items()) if v == max_ppl]
    print(' '.join(max_hrs))

# Sample Test
import os, IsoContestTest
file_path = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))
data_path = file_path + os.sep  + '3'
IsoContestTest.print_test_result(data_path, solution)
