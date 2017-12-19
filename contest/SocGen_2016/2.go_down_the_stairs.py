'''
Two people A and B stand at the top of a building. The elevator is out of order,
they decide to race to the last level of the basement. As you stand on the
ground floor, you would like to determine which one will go through the ground
floor first.

To achieve this, you will be given the number of steps from the top floor to
the ground floor and the chronology of their actions.

Data

Input
Row 1: an integer S between 10 and 10000 representing the number of steps from
    the top of building to the ground floor.
Row 2: an integer N between 1 and 2000 representing the number instants in the
    chronology.
Row 3 to N + 2 : an integer X and an integer Y space separated where X
    represents the number of steps by which A went down at instant t and Y
    represents by which B went down at instant t.

The chronology will always enable A or B to reach the ground floor (and even to
continue towards the last level of the basement).

Output
The name of the first person go through the ground floor (ie A or B). If they
arrive at the same instant, display: NO WINNER.
'''
def solution(lines):
    s = int(lines[0])
    x = y = 0
    for line in lines[2:]:
        x += int(line.split()[0])
        y += int(line.split()[1])
        if x >= s and y >= s:
            print('NO WINNER')
            break
        elif x >= s > y:
            print('A')
            break
        elif x < s <= y:
            print('B')
            break

# Sample Test
# Sample Test
import os, IsoContestTest
q = 2
test_data_path = "{0}{1}{2}".format(os.path.abspath(os.path.dirname(os.path.realpath(__file__))), os.sep, q)
IsoContestTest.print_test_result(test_data_path, solution)
