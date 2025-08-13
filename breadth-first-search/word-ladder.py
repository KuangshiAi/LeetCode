class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        word_set = set(wordList)
        if endWord not in word_set:
            return 0
        if beginWord == endWord:
            return 1

        q = deque([(beginWord, 1)])  # (word, number_of_words_in_path)
        if beginWord in word_set:
            word_set.remove(beginWord)

        while q:
            word, steps = q.popleft()
            for i in range(len(word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    if c == word[i]:
                        continue
                    nw = word[:i] + c + word[i+1:]
                    if nw == endWord:
                        return steps + 1
                    if nw in word_set:
                        word_set.remove(nw)
                        q.append((nw, steps + 1))
        return 0
        