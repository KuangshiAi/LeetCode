class Solution(object):
    def makeStringGood(self, s):
        freq = [0] * 26
        for char in s:
            freq[ord(char)-ord('a')] += 1
        def dp(i, deleted, target):
            if i == 26:
                return 0
            x = freq[i]
            if x == target or x==0:
                return dp(i+1, 0, target)
            elif x > target:
                return dp(i+1, x-target, target) + x - target
            else:
                goal = target - x
                insert = dp(i+1, 0, target) + goal
                delete = dp(i+1, x, target) + x
                change = dp(i+1, 0, target) + goal - min(goal, deleted)
                return min(insert, delete, change)

        mini = float('inf')
        for target in range(max(freq) + 1):
            mini = min(mini, dp(0,0,target))
        return mini