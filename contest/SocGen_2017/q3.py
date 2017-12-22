'''
Problem Statement

As a developer from the country side, you have a totally rational fear of heights. However you also have a totally rational yearning for a fiber-optic connection to the Internet. Thus, you decide to move to one of the big cities where fiber-optic is available, but you want to avoid tall skyscrapers as much as possible. Consequentyly, you want to move to the city with the lowest skyline, that is, the city in which the tallest building is as low as possible.

Data

Input

Row 1: an integer N comprised between 1 and 1000 representing the number of cities.
Row 2: an integer M comprised between 1 and 1000 representing the number of buildings given per city (which is the same for every city).
Row 3 to N + 2: a sequence of M space-separated integers comprised between1 and 1,000,000 representing the height of the buildings in a given city. If we call i the row number, then the index of the city is i-3.

Output

An integer between 0 and N-1 representing the index of the city you will move to. If two cities'skyline have the same highest building that is also the lowest highest building among all cities, both answers will be accepted.
'''

def solution(lines):
    building_heights_max = [max(map(int, l.split())) for l in lines[2:]]
    min_height = min(building_heights_max)
    print(building_heights_max.index(min_height))


# Sample Test
import os, IsoContestTest
q = 3
test_data_path = "{0}{1}{2}".format(os.path.abspath(os.path.dirname(os.path.realpath(__file__))), os.sep, q)
IsoContestTest.print_test_result(test_data_path, solution)
