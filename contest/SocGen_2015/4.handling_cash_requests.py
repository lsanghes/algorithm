'''
Objective

When a cash dispenser handles a cash request, a classical method is to provide
in priority the largest note then to provide smaller notes to cover the rest of
the request and to continue like this until the request is filled.

Example : if the request is $190 and the cash dispenser has $100, $50, $20, and
$10 notes, the cash dispenser will provide a $100 note and a $50 note and 2 $20
notes.

In this challenge, you will be provided with a cash request and the list of
available notes and you will have to determine the notes that the dispenser
provides according to the above algorithm. You can assume that the dispenser
has a sufficient quantity of each notes to fill the withdrawal.

The challenge will not use realistic data, notes can have value like 12311 and
the withdrawal can be very high.

Data Format

Input
Row 1 : an integer between 1 and 100,000 representing the amount that you have
to deliver.
Row 2 : an integer N representing the number of types of notes that the cash
dispenser can use.
Row 3 to N+2 : an integer between 1 and 50,000 representing the face values of
the notes that are available. The notes are sorted ascendingly.

You can assume that the dispenser will always hold the right notes to match the
withdrawal.

Output

A series of pairs of integers Xi and Yi separated by a space. For each type of
note used to fill the order, Xi represents the number of notes of value Yi that
you want to deliver. The pairs have to be sorted in descending order of Yi. If
we take the example above, the output would be :
1 100 1 50 2 20
'''
def solution(lines):
    inputs = iter(lines)
    amount = int(next(inputs))
    types = int(next(inputs))
    vals = []
    for _ in range(types):
        vals.append(int(next(inputs)))
    d = {}
    for note_val in vals[::-1]:
        count, amount = divmod(amount, note_val)
        if count:
            d[note_val] = count
    output = []
    for face_val, count in sorted(d.items())[::-1]:
        output.append(str(count))
        output.append(str(face_val))
    print(' '.join(output))

# Sample Test
import os, IsoContestTest
file_path = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))
data_path = file_path + os.sep  + '4'
IsoContestTest.print_test_result(data_path, solution)
