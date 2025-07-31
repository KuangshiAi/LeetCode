class Solution(object):
    def makeStringGood(self, s):
        """
        :type s: str
        :rtype: int
        """
        freq = [0]*26
        for char in s:
            freq[ord(char)-ord('a')] += 1

        memo = {}
        def dp(i, deleted, target):
            key = (i, deleted, target)
            if key in memo:
                return memo[key]
            if i == 26:
                return 0
            x = freq[i]
            if x == target:
                res = dp(i+1, 0, target)
            elif x > target:
                res = dp(i+1, x-target, target) + x-target
            else:
                insert = dp(i+1, 0, target) + target - x
                delete = dp(i+1, x, target) + x
                change = dp(i+1, 0, target) + target - x - min(deleted, target - x)
                res = min(insert,delete,change)
            memo[key] = res
            return res
        
        mini = float('inf')
        for target in range(max(freq)+1):
            mini = min(mini, dp(0,0,target))
        return mini