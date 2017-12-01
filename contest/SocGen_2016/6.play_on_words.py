'''
Did you know? If we consider you can go from one word to another by changing
only one of its letters then BEER and CODE are only 5 words apart:

BEER
BEES
BEDS
BEDE
BODE
CODE

You are given two words and a dictionary, and you must find the shortest path
between those two words, made of words from the dictionary. Your solution must
be in the order of 4 million operations, which is O(N^2L).

Data format

Input
Row 1: an integer L between 2 and 4 that represents the number of letters of
the words included in the dictionary.

Row 2: a word of L letters, the beginning word.
Row 3: a word of L letters, the ending word.
Row 4: an integer N between 1 et 1000 that represents the number of words in
    the dictionary.
Row 5 to N+4: a word of L letters that belongs to the dictionary. All words in
    the dictionary are uppercase.

Output
The words that enable to go from the beginning word to the ending word,
separated by spaces (including the beginning word and the ending word). If
there are multiple answers display the smallest in alphabetical order (for
example if TIC TAC TAU and TIC TIU TAU are two possible solutions, display TIC
TAC TAU). If it is not possible to go from the beginning word to the ending
word then display IMPOSSIBLE.
'''
def findLadders(beginWord, endWord, wordList):
    from collections import defaultdict
    def mask_one_char(word):
        return [word[:i] + char + word[i+1:] for i in range(len(word))
                    for char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
                        if word[i] != char]
    wordList = set(wordList)

    # build a graph with level order, stop when reaching endWord
    graph = defaultdict(set) # initialize the graph
    level = set([beginWord])
    while level and endWord not in graph:
        next_level = set()
        for word in level:
            for new_word in mask_one_char(word):
                # new_wrod in current level is not in graph yet!
                if new_word in wordList and new_word not in graph and new_word not in level:
                    graph[word].add(new_word)
                    next_level.add(new_word)
        level = next_level

    # search all paths
    queue = [(beginWord, [beginWord])]
    res = []
    while queue:
        vertex, path = queue.pop()
        if vertex == endWord:
            res.append(path)
        for v in graph[vertex] - set(path):
            queue.append((v, path + [v]))
    return sorted(res)

def solution(lines):
    L = lines[0]
    begin = lines[1]
    end = lines[2]
    N = lines[3]
    dictionary = set(lines[4:])
    res = findLadders(begin, end, dictionary)
    if not res:
        print('IMPOSSIBLE')
    else:
        print(' '.join(res[0]))

# Sample Test
import os, IsoContestTest
file_path = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))
data_path = file_path + os.sep  + '6'
IsoContestTest.print_test_result(data_path, solution)
