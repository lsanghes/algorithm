'''
In2016,we will celebrate 100 years of the father of information theory, Claude
Shannon. For his memory, you want to prepare something to share your love for
computer science with high school studen.
print(len(a))
print(len(b))

You want to explain precisely to students how QR codes work. However you
realize two things:- This protocol is actually much more complicated than
what you thought;

- Galois fields do not quite belong to the high school curriculum.
So, you want to expose a simpler version, in order to show to them how binary
works.

Your protocol can only encode and decode 8-letter words, under the form of a
8x8 image made of bits. Each letter of the word is coded by its binary
representation in the ASCII table, on one byte. Students are having fun and are
showing to you their 8x8 images, that you need now to decode.

Binary to integer conversion can be computed as follows : - 1001 in binary
equals 2^3 + 2^0 = 9

-10100111 in binary equals 2^7 + 2^5 + 2^2 + 2^1+ 2^0 = 128 + 32 + 4 +2 + 1=167
The ASCII code of the capital letter A is 65, B is 66,..., Z is 90.

Data format

Input
Rows 1 to 8: a string of 8 characters that may be 0 or 1, that represents a
    capital letter between A and Z coded in binary.

Output
The 8-letter decoded word.
'''
def solution(lines):
    res = ''
    for line in lines:
        res += chr(int(line, 2))
    print(res)

# Sample Test
import os, IsoContestTest
file_path = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))
data_path = file_path + os.sep  + '3'
IsoContestTest.print_test_result(data_path, solution)
