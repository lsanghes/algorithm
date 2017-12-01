'''
A trending topic is a Twitter hashtag that appears with a high frequency within
a certain period of time. In this challenge, we will consider that a hashtag
needs to appear at least 40 times in a 60 minutes period to be considered as a
trending topic.

In this challenge, you need to determine if there is a trending topic in a
hashtag flow. Hashtag in the flow are separated by one minute, so there are 60
tags in a 60 minutes flow.

Data format

Input
Row 1: an integer N comprised between 1 and 1000 corresponding to the number of
    hashtags in the flow.
Rows 2 to N+1: a Twitter hashtag. A hashtag contains only non-accentuated
    lowercase characters and starts with the # symbol.

Output
A string (starting with the # symbol) corresponding to the first
(chronologically) trending topic, if any, otherwise the string No trending topic
'''
def solution(lines):
    from collections import Counter
    inputs = iter(lines)
    tags = lines[1:]
    res = 'Pas de trending topic'
    counter = Counter()
    for i, tag in enumerate(tags):
        counter[tag] += 1
        if i >= 60:
            counter[tags[i-60]] -= 1
        k, v = counter.most_common(1)[0]
        if v >= 40:
            res = k
            break
    print(res)

# Sample Test
import os, IsoContestTest
file_path = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))
data_path = file_path + os.sep  + '4'
IsoContestTest.print_test_result(data_path, solution)
