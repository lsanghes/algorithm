'''
Problem Statement

xTwo teams of great scientists have discovered replicas of the Attesor Enots, an artifact considered to be at the very pinnacle of the Naitpyge civilization. On this artifact was a text without any spaces which, despite its age, was written using the 26 letters of the Latin alphabet. The very same text was found on the replicas. However time took its toll and both replicas are incomplete, only parts of the text remain.

xCompared to the original artifact, several letters have disappeared, but the order of the remaining letters is unchanged. You are asked to reconstruct the original text from the two damaged replicas. But aligning the two texts to fill the blanks won't work at all: the engraving technology was too primitive to ensure a consistent width for the letters. Thus, since you have no information as to the amount of missing characters, you figure your best guess should be a text as short as possible such that the texts on both replicas can be obtained by removing some letters. In other words, all the letters appearing in each replica should also appear in your tentative reconstruction, in the same order.

Note: The expected algorithm should run in quadratic time.

Example

Given the input:
3
abc
4
dbcb

Possible answers are adbcb and dabcb. Note that for this input, there isn't any other possible string of length 5.

Data

Input

Row 1: an integer N comprised between 1 and 100 representing the number of letters on the first replica.
Row 2: a string of N lowercase letters found on the first replica.
Row 3: an integer M comprised between 1 and 100 representing the number of letters on the second replica.
Row 4: a string of M lowercase letters found on the second replica.

Output

A sxtring of lowercase letters, of minimum length, from which each replica can be obtained by deleting some of its letters.
'''

def fill_table(X, Y):
    m, n = len(X), len(Y)
    M = [[0]*(m+1) for i in range(n+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1] == Y[j-1]:
                M[j][i] = M[j-1][i-1] + 1
            else:
                M[j][i] = max(M[j][i-1], M[j-1][i])
    return M

def longest_common_substring(M, X, Y, i, j):
    if i == 0 or j == 0:
        return ""
    elif X[i-1] == Y[j-1]:
        return longest_common_substring(M, X, Y, i-1, j-1) + X[i-1]
    elif M[j-1][i] > M[j][i-1]:
        return longest_common_substring(M, X, Y, i, j-1)
    else:
        return longest_common_substring(M, X, Y, i-1, j)

def solution(lines):
    X, Y= lines[1], lines[3]
    M = fill_table(X, Y)
    lcs = longest_common_substring(M,X,Y,len(X),len(Y))

    res = ''
    xi = yi = 0
    for common_char in lcs:
        while X[xi] != common_char:
            res += X[xi]
            xi += 1
        xi += 1

        while Y[yi] != common_char:
            res += Y[yi]
            yi += 1
        yi += 1

        res += common_char

    while xi < len(X):
        res += X[xi]
        xi += 1

    while yi < len(Y):
        res += Y[yi]
        yi += 1

    print(res)


# Sample Test
import os, IsoContestTest
q = 7
test_data_path = "{0}{1}{2}".format(os.path.abspath(os.path.dirname(os.path.realpath(__file__))), os.sep, q)
IsoContestTest.print_test_result(test_data_path, solution)
