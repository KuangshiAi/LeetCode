class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        hashmap = {} # the last time s[i] appears
        if s == "":
            return 0
        res = 1
        dp = 0 # the longest non-repeating substring that ends at s[i]
        for i in range(len(s)):
            if s[i] in hashmap:
                if i - hashmap[s[i]] <= dp:
                    dp = i - hashmap[s[i]]
                else:
                    dp += 1
            else:
                dp += 1
            hashmap[s[i]] = i
            res = max(res, dp)
        return res

        