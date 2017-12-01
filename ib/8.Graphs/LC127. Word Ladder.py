'''
Given two words (beginWord and endWord), and a dictionary's word list, find the
length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time
Each intermediate word must exist in the word list
For example,

Given:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Note:
Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
'''
class Solution:
    # simple bfs with memo.
    def ladderLength(self, beginWord, endWord, wordList):
        from collections import deque
        if beginWord == endWord: # IB's invalid case
            return 1
        if type(wordList) == type([]): # IB input is []
            wordList = set(wordList)
        def mask_one_char(word):
            return [word[:i] + char + word[i+1:] for i in range(len(word))
                        for char in 'abcdefghijklmnopqrstuvwxyz'
                            if word[i] != char]
        wordList.discard(beginWord) # completely optional
        wordList.add(endWord) # endWord must be in dict to terminate
        queue = deque([(beginWord, 1)])
        while queue:
            word, step = queue.popleft()
            if word == endWord:
                return step
            for new_word in mask_one_char(word):
                if new_word in wordList:
                    queue.append((new_word, step + 1))
                    wordList.remove(new_word) # same as keeping visisted set
        return 0

    # bidirectional bfs with memo - fast!
    def ladderLength2(self, beginWord, endWord, wordList):
        if beginWord == endWord: # IB's invalid case
            return 1
        if type(wordList) == type([]): # IB input is []
            wordList = set(wordList)
        def mask_one_char(word):
            return [word[:i] + char + word[i+1:] for i in range(len(word))
                        for char in 'abcdefghijklmnopqrstuvwxyz'
                            if word[i] != char]
        front, back = set([beginWord]), set([endWord])
        wordList.discard(beginWord) # discard does not raise exeception
        wordList.discard(endWord) # discard does not raise exeception
        length = 2
        while front:
            if len(front) > len(back):
                front, back = back, front
            nextFront = set()
            for word in front:
                for new_word in mask_one_char(word):
                    if new_word in back:
                        return length
                    elif new_word in wordList:
                        nextFront.add(new_word)
                        wordList.remove(new_word) #same as keeping visisted set
            length += 1
            front = nextFront
        return 0

# test
print(Solution().ladderLength('hit','cog',['hot','dot','dog','lot','log']))
print(Solution().ladderLength('ab','bc',['ac']))
print(Solution().ladderLength('ab','ac',['ad,ae']))
print(Solution().ladderLength('bb','bb',['ba','ab']))
print(Solution().ladderLength('ab','de',['bc']))
print(Solution().ladderLength2('hit','cog',['hot','dot','dog','lot','log']))
print(Solution().ladderLength2('ab','bc',['ac']))
print(Solution().ladderLength2('ab','ac',['ad,ae']))
print(Solution().ladderLength2('bb','bb',['ba','ab']))
print(Solution().ladderLength2('ab','de',['bc']))
