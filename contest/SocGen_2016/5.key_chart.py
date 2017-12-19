'''
The security system of your building is simple. Doors have a given security
level. To open a door, you need either the specific key for this door or a key
that has a security level strictly higher than the key for this door. In this
challenge, you need to determine the minimum security level of the master key,
that is the key that can open all the doors.

You are provided with relative information in the form of "key for door A has
higher security level than key for door B". If a key never appears as having a
higher security level than any other key then its security level is 1.

There will always be a uniquer master key that is the unique solution to the
data that you are given. To determine the level of the master key, you must
assume that there is no empty security level i.e. that there is a least one key
for each security level.

Example 1
If you are given the information:- Key for door A has a greater security level
than key for door B
- Key for door A has a greater security level than key for door CThen doors B
and C have a security level of 1 and the master key is the key for door A and
has a security level of 2.

Example 2
If you are given the information:- Key for door A has a greater security level
than key for door B
- Key for door B has a greater security level than key for door CThen door C
has a security level of 1. Key for door B has a security level of 2. And the
master key is the key for door A and has a security level of 3.

Data format

Input
Row 1: an integer N between 1 and 1000 which represents the number of rows in
    the key chart.
Row 2 to N+1: two space-separated door identifiers A and B, indicating that the
    key for door A has a higher security level than the key for door B. All
    door identifiers contain at most 50 alphanumeric and underscore characters,
    lowercase.

Output
The minimal security level of the key that can open all the doors.
'''
def update_parent(node, counter, parent):
    for p in parent[node]:
        if p in counter:
            counter[p] = max(counter[p], counter[node]+1)
        else:
            counter[p] = counter[node]+1
        update_parent(p, counter, parent)

def solution(lines):
    counter = {}
    parent = {}
    for line in lines[1:]:
        a, b = line.split()
        if a not in parent:
            parent[a] = []
        if b not in parent:
            parent[b] = [a]
        else:
            parent[b].append(a)
    for line in lines[1:]:
        a, b = line.split()
        if b not in counter:
            counter[b] = 1
        if a not in counter:
            counter[a] = counter[b] + 1
        else:
            counter[a] = max(counter[b] + 1, counter[a])
            update_parent(a, counter, parent)
    print(max(counter.values()))

# Sample Test
import os, IsoContestTest
q = 5
test_data_path = "{0}{1}{2}".format(os.path.abspath(os.path.dirname(os.path.realpath(__file__))), os.sep, q)
IsoContestTest.print_test_result(test_data_path, solution)
