'''
You are given a string, s, and a list of words, words, that are all of the same
length. Find all starting indices of substring(s) in s that is a concatenation
of each w in words exactly once and without any intervening characters.

For example, given:
s: "barfoothefoobarman"
words: ["foo", "bar"]

You should return the indices: [0,9].
(order does not matter).
'''
class Solution:
    # SubStringTwoPointerTemplate.py
    # [j,k+w_len-1] is the valid window containing each word once
    def findSubstring(self, s, words):
        from collections import defaultdict
        res = []
        word_len = len(words[0])
        total_len = len(words) * word_len
        d = defaultdict(int)
        for w in words: # build hashmap
            d[w] += 1
        for j, k in [(i,i) for i in range(word_len)]:
            dcopy = d.copy() # new hashmap for each i
            while k < len(s) - word_len + 1: # stop at last possible index
                w = s[k:k+word_len] # current word
                dcopy[w] -= 1
                while dcopy[w] < 0: # w is invalid
                    dcopy[s[j:j+word_len]] += 1
                    j += word_len # move j till next valid word
                if k + word_len - j == total_len:
                    res.append(j)
                k += word_len
        return res

    # bruteforce hashing all words permutations - TLE
    def findSubstring2(self, s, words):
        from itertools import permutations
        res  = []
        word_len = len(words[0])
        total_len = word_len * len(words)
        targets = {''.join(p) for p in permutations(words, len(words))}
        for i in range(len(s) - word_len + 1):
            w = s[i:i+total_len]
            if w in targets:
                res.append(i)
        return res

    # rolling hash sum
    # if hash(a1) + hash(a2) = hash(b1) + hash(b2) then set(a1,a2) = set(b1,b2)
    # not always True there could be potential hash collision
    # hash collision occurs for python 2.7 but working fine for python 3.5
    def findSubstring3(self, s, words):
        word_len = len(words[0])
        total_len = len(words) * word_len
        target_hash = sum([hash(w) for w in words])
        hashes = [hash(s[i:i+word_len]) for i in range(len(s)-word_len+1)]
        res = []
        for j in range(word_len):
            k = j + total_len - 1 # [j,k] is the rolling window size
            while k < len(s):
                hash_sum = sum([hashes[i] for i in range(j, k+1, word_len)])
                if hash_sum == target_hash:
                    res.append(j) # we may do safe check for collision
                j += word_len
                k += word_len
        return res

# test
testdata=[("abbbbbacbc",["bc","ac"]),
          ("aaaaaa",["aaa","aaa"]),
          ("aaaaaaaa",["aa","aa","aa"]),
          ("barfoothefoobarman",["foo","bar"]),
          ("barfoofoobarthefoobarman",["bar","foo","the"]),
          ("lingmindraboofooowingdingbarrwingmonkeypoundcake",["fooo","barr","wing","ding","wing"])]
for s, w in testdata:
    print(Solution().findSubstring(s, w))
    print(Solution().findSubstring2(s, w))
    print(Solution().findSubstring3(s, w))
