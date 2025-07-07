class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        dic = {} # the last place where s[i] appears
        i = -1
        for j in range(len(s)):
            if s[j] in dic:
                i = max(i, dic[s[j]])
            dic[s[j]] = j
            res = max(res, j-i)
        return res
        