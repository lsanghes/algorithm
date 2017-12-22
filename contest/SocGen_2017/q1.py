'''
Subject

You are in charge of writing an algorithm of automatic trading. One of the inputs of the algorithm is the number of trades that have been performed since the beginning of the day. For this purpose, the day is decomposed in time intervals and you receive the number of trades that took place during each interval.

Data format

Input
Row 1: an integer number comprised between 10 and 1000 representing the the number of time intervals.
Row 2 to N+1: an integer number comprised between 0 and 15 representing the number of trades that took place during each time interval.

Output
An integer representing the total number of trades that took place.
'''

def solution(lines):
    print(sum([int(l) for l in lines[1:]]))


# Sample Test
import os, IsoContestTest
q = 1
test_data_path = "{0}{1}{2}".format(os.path.abspath(os.path.dirname(os.path.realpath(__file__))), os.sep, q)
IsoContestTest.print_test_result(test_data_path, solution)
