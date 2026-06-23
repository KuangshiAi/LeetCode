class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        outcome=''
        for i in range(min(len(word1), len(word2))):
            outcome += word1[i]
            outcome += word2[i]
        if len(word1) <= len(word2):
            outcome += word2[len(word1):]
        else:
            outcome += word1[len(word2):]
        return outcome