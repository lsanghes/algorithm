'''
In this challenge, you must display the 5 most common tags from a blog.

Data format
Input
- Line 1: an integer N between 15 and 800 representing the total number of tags.
- Line 2 to N + 1: a tag of the blog.

Tags are composed of lowercase letters without accents. There are at least five
different tags. There is no tie (ie 2 tags appearing the same number of times).

Output
5 lines each containing a tag and an integer X P separated by a space.
P represents the number of times the X tag will appear in the blog. The first
line contains the tag which is the most common, the second line contains the
second most common tag and so on until the 5th.
'''
# Sample Code
def solution(lines):
    from collections import Counter
    counter = Counter(lines[1:])
    for tag, count in counter.most_common(5):
        print('{} {}'.format(tag, count))

# Sample Test
import os, IsoContestTest
q = 2
test_data_path = "{0}{1}{2}".format(os.path.abspath(os.path.dirname(os.path.realpath(__file__))), os.sep, q)
IsoContestTest.print_test_result(test_data_path, solution)
