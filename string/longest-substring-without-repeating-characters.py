class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # res = 0
        # dic = {} # the last place where s[i] appears
        # i = -1
        # for j in range(len(s)):
        #     if s[j] in dic:
        #         i = max(i, dic[s[j]])
        #     dic[s[j]] = j
        #     res = max(res, j-i)
        # return res

        # dp[i]: the length of the longest non-reapting substring ends with s[i]
        i = -1
        res = 0
        dp = 0
        dic = {}
        for j in range(len(s)):
            i = dic.get(s[j], -1)
            dic[s[j]] = j
            if dp < j-i:
                dp += 1
            else:
                dp = j-i
            res = max(res, dp)
        return res
        