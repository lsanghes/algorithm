'''
One of the tasks of a developer SalesForce is to qualify its database to allow
business to work with the relevant information.

In this challenge, you must validate the records from extraction of the base.
To be valid, a record must meet three criteria: it must not match a duplicate,
the size of the phone must be valid and must belong to your area. How to
assess the criteria are:

- Two lines are considered duplicates if they have the same name and company.
- A phone number is valid if it has the following format + X-yyyyyyyyyyy where
    X is a sequence of 1 and 3 digit yyyyyyyyyyy is a suite of 9 11-digit.
    For a number to be valid it must contain the + character before
    and X - between X and Y.

- Your area is a set of countries. The record corresponds to your area if his
    country is included in your country list.

Data format
Input
Line 1: an integer N between 5 and 500 representing the number of lines in
    the extraction.
Line 2: The list of countries in your area represented by a series of chains
    unaccented lowercase. The strings are separated by; (semicolon).
Line 3 to N + 2: the name, company, phone and client countries separated by;
    (semicolon). Information is composed by: unaccented lowercase letters,
    numbers and characters - and +.

Output
3 integers X Y Z separated by spaces.
X is an integer representing the number of duplicates
Y is an integer representing the number of records including an incorrect
    phone format
Z is an integer representing the number of records outside your area.

If a line appears k times while it accounts for k-1 duplicates.

Recording with both a phone and a wrong country outside your area should be
counted to determine Y and Z. By cons, if a record exists then the duplicate
or subsequent occurrences of the record should be ignored and not should not
be taken into account in determining Y, and Z.
'''
# Sample Code
def solution(lines):
    import re
    n = int(lines[0])
    my_areas = set(lines[1].split(';'))
    memo = set()
    dup, wrong_format, outside_area = 0, 0, 0
    for line in lines[2:]:
        first, last, company, phone, country = line.split(';')
        key = (first, last, company)
        if key in memo:
            dup += 1
            continue
        memo.add(key)
        if country not in my_areas:
            outside_area += 1
        if not re.search('^\+\d{1,3}-\d{9,11}$', phone):
            wrong_format += 1
    print(str(dup) + ' ' + str(wrong_format) + ' ' + str(outside_area))

# Sample Test
import os, IsoContestTest
file_path = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))
data_path = file_path + os.sep  + '3'
IsoContestTest.print_test_result(data_path, solution)
