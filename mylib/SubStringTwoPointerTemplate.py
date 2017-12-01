'''
https://discuss.leetcode.com/topic/30941/here-is-a-10-line-template-that-can-solve-most-substring-problems/6

# lc003   - Longest Substring Without Repeating Characters
# lc030  - Substring with Concatenation of All Words
# lc076  - Minimum Window Substring
# lc159 - Longest Substring with At Most Two Distinct Characters
'''
def findSubstring(self, s):
    from collections import defaultdict
    counter = ? # check whether the substring is valid
    j, k = 0, 0 # two pointers, one point to tail and one head
    sub_len = ?  # intial len of substring, N+1 for minimum, and 0 for maximum
    d = defaultdict(int)
    for: d[x] = ? # set up the hashmap d
    while k < len(s):
        if d[s[k]] > 0:
            counter -= 1 # modify counter here
        d[s[k]] -= 1
        while counter ? : # counter condition
            # update sub_len here if finding SHORTEST
            # sub_len = ? if ? else ?

            # increase j to make it invalid/valid again
            d[s[j]] += 1
            if d[s[j]] > 0:
                counter += 1 # modify counter here
            j += 1

        # update sub_len here if finding LONGEST
        # sub_len = ? if ? else ?
        k += 1
    return sub_len
