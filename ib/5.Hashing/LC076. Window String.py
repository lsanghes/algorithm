'''
Given a string S and a string T, find the minimum window in S which will contain
all the characters in T in complexity O(n).

For example,
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC".

Note:
If there is no such window in S that covers all characters in T, return the
empty string "".

If there are multiple such windows, you are guaranteed that there will always
be only one unique minimum window in S.
'''
class Solution:
    # @param s : string
    # @param t : string
    # @return a string

    # SubStringTwoPointerTemplate.py
    # Use two pointers j and k to represent a window.
    # Move k to find a valid window.
    # When a valid window is found, move j to find a smaller window.
    def minWindow(self, s, t):
        from collections import defaultdict
        d = defaultdict(int)
        for char in t:
            d[char] += 1
        j = k = 0
        min_start, min_len = 0, len(s)+1
        counter = len(t)
        while k < len(s):
            if d[s[k]] > 0: # found a valid char
                counter -= 1 # reduce total char needed
            d[s[k]] -= 1
            while counter == 0:
                if k-j+1 < min_len:
                    min_start, min_len = j, k-j+1
                d[s[j]] += 1 # now move j forward
                if d[s[j]] > 0: # s[j] is in t
                    counter += 1
                j += 1
            k += 1
        return s[min_start: min_start + min_len] if min_len <= len(s) else ''

    # all nums are in window when all the counts are <= 0
    # defaultdict(int) is much faster than Counter but still TLE
    def minWindow2(self, s, t):
        from collections import defaultdict
        d = defaultdict(int)
        for char in t:
            d[char] += 1
        j = k = 0
        min_start, min_len = 0, len(s)+1
        while k < len(s):
            char = s[k]
            d[char] -= 1
            while not [n for n,c in d.items() if c > 0]:
                # found valid window! increment j till windows become invalid
                if k-j+1 < min_len:
                    min_start = j
                    min_len = k-j+1
                d[s[j]] += 1
                j += 1
            k += 1
        return s[min_start: min_start + min_len] if min_len <= len(s) else ''

# test
# A  D  O  B  E  C  O  D  E  B  A  N  C
# 0  1  2  3  4  5  6  7  8  9  10 11 12
print(Solution().minWindow('ADOBECODEBANC', 'ABC'))
print(Solution().minWindow('ADOBECODEBANC', 'ABC.'))
print(Solution().minWindow2('ADOBECODEBANC', 'ABC'))
print(Solution().minWindow2('ADOBECODEBANC', 'ABC.'))
