'''
Problem Statement

Octetcoin is a new cryptocurrency like bitcoin, but instead of using outdated bits, it uses octets so that you can earn your cryptocurrency 8 times faster. Furthermore octetcoin is centralized, OctetCorp excavates the variation of the USD-octetcoin exchange rate in the blockchain at regular intervals.You noticed that the variations of the exchange rate for the seconds to come are stored in the javascript of their homepage (you just happen to like reading random uncommented javascript). The exchange rate variations are all signed integers (cents won't be supported until hexcoin) indicating how much value an octetcoin gains (or loses) with each new excavation.

You want to show your friends you are a first rate investor before octetcoin crash to its demise. So, you want to buy a single octetcoin and sell it at the perfect time to maximize your profit. There is always a profit to be made, the question is how much money can you make out of this?

Example

Given the input:
5
-2
3
-1
2
-8


The first row 5 represents the number of blocks, the following 5 represent indicate the variations of the value.
For this input, the answer is 4, you first wait for the value to decrease by -2 then buy your octetcoin before it raises again by 3, you sell it before the crash of -8, thus earning 3-1+2=4.
Note that you can not buy and sell your octetcoin multiple times, so you can not sell it before -1 and rebuy it afterward to earn more.

Given the very large size of the input, an algorithm of linear complexity is required. Quadratic solutions will take too much time.

Data format

Input
Row 1: an integer N between 1 and 200000, the size of the blockchain before octocorp is incriminated.
Row 2 to N+1: an integer between -100 and 100 representing the variation of the exchange rate.

Output
An integer representing the maximum profit you can make from the given blockchain.
'''

def solution(lines):
    local_max = glb_max = 0
    price_changes = map(int, lines[1:])
    for p in price_changes:
        local_max = max(0, local_max + p)
        glb_max = max(glb_max, local_max)
    print(glb_max)


# Sample Test
import os, IsoContestTest
q = 5
test_data_path = "{0}{1}{2}".format(os.path.abspath(os.path.dirname(os.path.realpath(__file__))), os.sep, q)
IsoContestTest.print_test_result(test_data_path, solution)
