'''
In this challenge, you need to plug multiple extension cords together in order
to get the greatest possible length. Extension cords can have various types:
male-female, female-male, female-female, male-male. The extension cord that you
will create by assembling multiple extension cords will need to have a male
termination at one end and a female termination at the other end.

Data format

Input
- Row 1: an integer N comprises between 1 and 1000 representing the number of
    extension cords.
- Row 2 to N+1: a string comprising 3 characters and an integer number between
    1 and 50 separated by a space. The string corresponds to the extension cord
    type: M-M, F-M, M-F or F-F and the integer number represents its length.

Output
An integer number representing the length of the longest extension cord that
can be created by assembling the extenders together and that has a male
termination on one end and a female termination on the other end.
'''
def solution(lines):
    inputs = iter(lines)
    res = 0
    mm, ff = [], []
    mf_len = 0
    for line in lines[1:]:
        cord, length = line.split()
        if cord in ('M-F', 'F-M'):
            mf_len += int(length)
        elif cord == 'M-M':
            mm.append(int(length))
        elif cord == 'F-F':
            ff.append(int(length))
    min_len = min(len(mm), len(ff))
    ff.sort(reverse=True)
    mm.sort(reverse=True)
    total_len = mf_len + sum(ff[:min_len]) + sum(mm[:min_len])
    print(total_len)

# Sample Test
import os, IsoContestTest
q = 5
test_data_path = "{0}{1}{2}".format(os.path.abspath(os.path.dirname(os.path.realpath(__file__))), os.sep, q)
IsoContestTest.print_test_result(test_data_path, solution)
