class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # start, end = 0, 0
        # def expand(l,r,s):
        #     while l >= 0 and r < len(s) and s[l] == s[r]:
        #         l -= 1
        #         r += 1
        #     return l+1, r-1
        # for i in range(len(s)):
        #     l1,r1 = expand(i,i,s)
        #     l2,r2 = expand(i,i+1,s)
        #     if r1-l1 > end - start:
        #         start = l1
        #         end = r1
        #     if r2-l2 > end - start:
        #         start = l2
        #         end = r2
        # return s[start:end+1]

        # dp[i][j]: s[i:j+1] is palindromic
        dp = [[False]*len(s) for _ in range(len(s))]
        start, max_len = 0, 1
        for i in range(len(s)):
            dp[i][i] = True
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                start = i
                max_len = 2
        for length in range(3, len(s)+1):
            for i in range(len(s)-length+1):
                j = i + length -1
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    start = i
                    max_len = length
        return s[start:start+max_len]