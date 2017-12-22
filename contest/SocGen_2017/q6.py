'''
Problem Statement

You are a big user and fan of megasoft corporation products, one of them being FAT16 which currently is the most futuristic file system there is. However, since the future is now, you think you can do better and start to design FAT17.

Your computer has a single drive C: which is at the root of a directory hierarchy. A directory on your computer can be identified by its path: C: followed by the name of all the directories you have to traverse to reach it. In a path, all names are separated by \ such as C:\WINDOWS\SYSTEM32. Furthermore, a directory name is written using digits and capital letters only (all other unicode characters are useless anyway) and there can not be two directories with the same name anywhere within the hierarchy (we are not that much into the future yet).

You have stored the directory hierarchy as a list of pairs: when a directory FOO contains another directory BAR, you write FOO BAR in your system file.
For obvious reasons, all directories appear exactly once on the right hand side except C: which is the common ancestor of all directories.

Still, you are a visionary not a madman, there is no way your i9 CPU will handle long paths such as the 19 characters long C:\WINDOWS\SYSTEM32.
As a result, you have to write a tool which will give you one of the longest paths in your file system.

Note: the time complexity of your algorithm should be at most quadratic (but it is possible to do even better!).

Example

Given the input:
5
C: WINDOWS
FOO BAR
WINDOWS SYSTEM32
C: FOO
BAR XYZZY


The answer is C:\WINDOWS\SYSTEM32 since its length 19 is greater than 16 (the length of C:\FOO\BAR\XYZZY).

Data format

Input
Row 1: an integer N comprised between 1 and 1000 representing the number of rows in your system file.
Row 2 to N+1: 2 space separated strings comprising between 1 and 32 characters reprsententing directory names, the first being the parent directory of the second.

You are guaranteed that the names of the directories are globally unique: even directories with distinct parents must have different names. The directory names only use alphanumeric characters, but the name of your drive C: contains a colon.

Output
A string of maximum length among the full paths of the existing directories.
'''

def solution(lines):
    from collections import defaultdict
    graph = defaultdict(set)
    for l in lines[1:]:
        p, c = l.split()
        graph[p].add(c)

    begin = "C:"
    max_len, max_path = len(begin), []

    stack = [(begin, [begin], len(begin))]
    while stack:
        vertex, path, length = stack.pop()
        if length > max_len:
            max_len, max_path = length, path
        for v in graph[vertex] - set(path):
            stack.append((v, path+[v], length+len(v)))
    print('\\'.join(max_path))


# Sample Test
import os, IsoContestTest
q = 6
test_data_path = "{0}{1}{2}".format(os.path.abspath(os.path.dirname(os.path.realpath(__file__))), os.sep, q)
IsoContestTest.print_test_result(test_data_path, solution)
