'''

Problem statement

Blackjack is a casino card game that is played by two: the dealer against you. The principle is simple. You draw cards one by one, trying to get closer to 21 while avoiding exceeding this value. If you get 21, you win the bet, that's a BLACK JACK! If you get a value below 21, you must compare your result with the dealer's to see if you win the bet. Otherwise, if your result is greater than 21, you lose your bet regardless of the dealer's result.

The casino is generous today, it considers that in case of equality with the dealer (including for a blackjack), you win the bet as long as your result is less than or equal to 21. In return, it requires you to draw three cards at each game and to consider the ace as having value 1 systematically.

The cards in the game are 1,2,3,4,5,6,7,8,9,10, J, Q, R with J, Q and R equal to 10.

Data

Input
Rows 1: Three space-separated values representing the dealer's three cards. Values can be integer numbers between 1 and 10 or a character (J, Q or R)
Rows 2: Three space-separated values representing your three cards. Values can be integer numbers between 1 and 10 or a character (J, Q or R)

Output
A string :
- BLACK JACK, if the total of your cards is equal to 21
-WIN, In two cases : a) if the sum of your cards is below 21 and greater than or equal to the sum of the croupier cards, or b) if the total of your cards is less than 21 and the total of the croupier cards is greater than 21.
-LOSE, In all other cases
'''

def val(c):
    return 10 if c in ["J", "Q", "R"] else int(c)

def solution(lines):
    dealer_cards = sum(map(val, lines[0].split()))
    my_cards = sum(map(val, lines[1].split()))
    if my_cards == 21:
        print("BLACK JACK")
    elif my_cards < 21 and my_cards >= dealer_cards:
        print("WIN")
    elif my_cards < 21 and dealer_cards > 21:
        print("WIN")
    else:
        print("LOSE")


# Sample Test
import os, IsoContestTest
q = 2
test_data_path = "{0}{1}{2}".format(os.path.abspath(os.path.dirname(os.path.realpath(__file__))), os.sep, q)
IsoContestTest.print_test_result(test_data_path, solution)
