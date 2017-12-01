'''
Let's start with an easy challenge... You just have to compute how much is left
on an account after a series of transactions. You are provided with an opening
balance, and then you get a series of transactions that either increase or
decrease the balance. Transactions will be represented by amounts, negative when
they reduce the balance and positive when they increase the balance.

You can assume that the balance will never be negative.

Data

Input
Row 1 : an integer between 50,000 and 100,000 representing the opening balance.
Row 2 : an integer N between 1 and 100 representing the number of transactions.
Row 3 to N + 2 : an integer between -1000 and 1000 representing a transaction.

Output
An integer representing the closing balance.
'''
def solution(lines):
    inputs = iter(lines)
    balance = int(next(inputs))
    n = int(next(inputs))
    for _ in range(n):
        balance += int(next(inputs))
    print(balance)

# Sample Test
import os, IsoContestTest
file_path = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))
data_path = file_path + os.sep  + '1'
IsoContestTest.print_test_result(data_path, solution)
