'''

Problem Statement

You just received as a gift a huge cake nearing its expiration date which is clearly too big to eat alone, so you decide to share half of it with your roommate. However, it turns out that the only kind of chocolate she likes is white chocolate. Despite your initial disbelief in the existence of such a person, you quickly realize that you can take advantage of that to keep most of the real chocolate for yourself.

The cake has a round shape and is decorated with regularly spaced chocolate chips (either dark chocolate or white chocolate) forming a circle. Your goal is to cut the cake in half such that your half of the cake has as many dark chocolate chips as possible.

To simplify the problem, we will represent the cake as a string where each character is either a white chip or a dark chip. Since the chips form a circle, they are multiple ways to represent the same layout depending on the starting point. For instance, xoooox and ooooxx both correspond to the same layout of chocolate chips, since the two strings are related by a circular permutation. And in such case, the answer would be 2.

Data format

Input
Row 1: an even integer N between 1 and 1000, the number of chocolate chips on the cake.
Row 2: a string of length N representing the layout of the cake: x for dark chocolate and o for white chocolate.

Output
An integer representing the maximum number of dark chocolate chips for this layout in one half of the cake (ie that includes N/2 chips in total).
'''

def val(c):
    return 1 if c == "x" else 0

def solution(lines):
    cake = [val(l) for l in lines[1]]
    half = len(cake)//2
    max_num = 0
    for i in range(half):
        a = sum(cake[:i]) + sum(cake[i+half:])
        b = sum(cake[i:i+half])
        max_num = max(max_num, a, b)
    print(max_num)


# Sample Test
import os, IsoContestTest
q = 4
test_data_path = "{0}{1}{2}".format(os.path.abspath(os.path.dirname(os.path.realpath(__file__))), os.sep, q)
IsoContestTest.print_test_result(test_data_path, solution)
