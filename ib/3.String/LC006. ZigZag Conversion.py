'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of
rows like this: (you may want to display this pattern in a fixed font for
better legibility)

P.......A........H.......N
..A..P....L....S....I...I....G
....Y.........I........R
And then read line by line: PAHNAPLSIIGYIR
Write the code that will take a string and make this conversion given a number
of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR"
**Example 2 : **
ABCD, 2 can be written as

A....C
...B....D
and hence the answer would be ACBD.
'''
class Solution:
    def convert(self, A, B):
        if B == 1 or B >= len(A):
            return A
        rows = [''] * B
        r, step = 0, -1 # -1 because it flips for the first letter
        for a in A:
            rows[r] += a
            if r == B-1 or r == 0:
                step *= -1 # flip the direction when reach top/bottom
            r += step
        return ''.join(rows)

# test
print(Solution().convert('PAYPALISHIRING', 3))
print(Solution().convert('PAYPALISHIRING', 5))
