'''
With the advent of new technologies, CCTV is becoming more powerful, and human rights are now part of the past (how wonderful!). It is now possible to track the position of each person in a crowd, seen from above on a map.

You are given the 2-dimensional positions of several people. You have to identify all people considered at risk, i.e., anyone who is too close to at least K people. Being too close means that the distance between two people is lower or equal to R.

As a reminder, the distance between two points of coordinates (X1,Y1) and (X2,Y2) is given by :

Data format

Input
Row 1: three space-separated numbers N, K and R. N is an integer between 1 and 1000 that represents the size of the crowd. K is an integer between 1 and N and is defined above. R is a floating number between 0 and 5 and is defined above.
Rows 2 to N+1: two space-separated integers between 1 and 100 that represent the coordonate of a person. Persons have IDs from 1 to N i.e the person on row 2 has ID 1, the person on row 45 has ID 44.

Output
If nobody is at risk, you must display No danger. Otherwise, you must display a series of space-separated integers that represent the IDs of people at risk. The IDs must be sorted ascendingly.
'''
def solution(lines):
    import collections, itertools
    # print(list(itertools.combinations([1,2,3], 2))) # C(n, k)
    N = int(lines[0].split()[0])
    K = int(lines[0].split()[1])
    R = float(lines[0].split()[2])
    counter = collections.defaultdict(int)
    # for i in range(1, len(lines)):
        # for j in range(i+1, len(lines)):
    for i, j in itertools.combinations(range(1, N), 2):
        x1,y1 = map(int, lines[i].split())
        x2,y2 = map(int, lines[j].split())
        d = ((x1-x2)**2 + (y1-y2)**2)**0.5
        if d <= R:
            counter[i] += 1
            counter[j] += 1
    output = sorted([k for k, v in counter.items() if v >= K])
    if output:
        print(' '.join(map(str, output)))
    else:
        print('No danger')

# Sample Test
import os, IsoContestTest
file_path = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))
data_path = file_path + os.sep  + '4'
IsoContestTest.print_test_result(data_path, solution)
