'''
In this challenge, you need to determine if a card number is valid. A card
number includes 16 digits:
- The first 6 correspond to the issuing bank,
- 9 digits are taken randomly,
- the last digit is the Luhne key

The Luhne key is based on the first 15 digits. One digit out of two is
multiplied by 2 starting with the first one. If the result is greater than 9
then 9 is deduced from the result. This provides a new series of digits. The
Luhne key is the value that needs to be added to this sum to get a number that
can be divided by 10.

Example: 5295 4648 5201 3672

By adding the Luhne Key (last digit of the card number), which is 2, to this
sum 68, you get the number 70, which is a multiple of 10. Therefore, this is a
valid card.

Data

Input
Row 1 : an integer N between 1 and 1000 indicating the number of credit card
numbers in the file.
Row 2 to N + 1 : a string of 16 digits representing a credit card number.

Output
An integer representing the number of valid credit cards numbers in the input.
'''
def solution(lines):
    inputs = iter(lines)
    n = int(next(inputs))
    valid_cards = 0
    for _ in range(n):
        number = [int(s) for s in next(inputs)]
        for i in range(0, 15, 2):
            num = number[i] * 2
            if num > 9:
                num -= 9
            number[i] = num
        if sum(number)%10 == 0:
    	    valid_cards += 1
    print(valid_cards)

# Sample Test
import os, IsoContestTest
file_path = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))
data_path = file_path + os.sep  + '2'
IsoContestTest.print_test_result(data_path, solution)
