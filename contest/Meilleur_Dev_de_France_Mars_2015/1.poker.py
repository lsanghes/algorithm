'''
In this challenge, you have to compute how much money a poker player holds at
the end of a game. The player has an initial amount. During each hand, the
player pays the starting pot X. Then he wins an amount Y being positive or nul.
So the change in his money during a hand is equal to -X+Y.

Your code needs to return the amount that the player holds at the end of the
game.

Data format

Input
Row 1 : an interger between 1,000 and 10,000 representing the initial amount
    that the player has.
Row 2 : an integer N between 10 and 45 representing the number of hands played.
Row 3 to N+2 : two positive integers separated by a space representing X and Y
    as defined above.

The input data will prevent the player from getting bankrupted and he will
always hold a positive amount of money.

Output
An integer representing the amount that the player holds the end of the game.
'''
def solution(lines):
    inputs = iter(lines)
    balance = int(next(inputs))
    n = int(next(inputs))
    for _ in range(n):
        line = next(inputs)
        x, y = line.split()
        balance += -int(x) + int(y)
    print(balance)

# Sample Test
import os, IsoContestTest
file_path = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))
data_path = file_path + os.sep  + '1'
IsoContestTest.print_test_result(data_path, solution)
