'''
Given a string,
find the length of the longest substring without repeating characters.

Example:

The longest substring without repeating letters for "abcabcbb" is "abc", which
the length is 3.

For "bbbbb" the longest substring is "b", with the length of 1.
'''
class Solution:
    # move the the left pointer to the right of previously repeated index
    def lengthOfLongestSubstring(self, s):
        memo = {}
        max_len = j = 0
        for k, char in enumerate(s):
            if char in memo:
                # pointer j can only move right! eg. "abba"
                j = max(j, memo[char]+1)
            memo[char] = k # update the index of last seen char
            max_len = max(max_len, k-j+1)
        return max_len

    # SubStringTwoPointerTemplate.py
    def lengthOfLongestSubstring2(self, s):
        from collections import defaultdict
        d = defaultdict(int)
        j, k, max_len, counter = 0, 0, 0, 0
        while k < len(s):
            if d[s[k]] > 0:
                counter += 1
            d[s[k]] += 1
            while counter > 0:
                d[s[j]] -= 1
                if d[s[j]] > 0: # s[j] is repeated
                    counter -= 1
                j +=1
            max_len = max(k-j+1, max_len)
            k += 1
        return max_len

# test
print(Solution().lengthOfLongestSubstring("abba"))
print(Solution().lengthOfLongestSubstring2("abba"))
print(Solution().lengthOfLongestSubstring("abcdeb"))
print(Solution().lengthOfLongestSubstring2("abcdeb"))
print(Solution().lengthOfLongestSubstring("abcabcbb"))
print(Solution().lengthOfLongestSubstring2("abcabcbb"))
