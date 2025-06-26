class Solution(object):
    def makeStringGood(self, s):
        count = [0] * 26
        for c in s:
            count[ord(c) - ord("a")] += 1

        memo = {}

        def dp(i, deleted, target):
            key = (i, deleted, target)
            if key in memo:
                return memo[key]

            if i == 26:
                return 0

            x = count[i]
            if x == target or x == 0:
                res = dp(i + 1, 0, target)
            elif x > target:
                res = dp(i + 1, x - target, target) + x - target
            else:
                need = target - x
                insert = dp(i + 1, 0, target) + need
                delete = dp(i + 1, x, target) + x
                change = dp(i + 1, 0, target) + need - min(deleted, need)
                res = min(insert, delete, change)

            memo[key] = res
            return res

        mini = float('inf')
        for target in range(max(count) + 1):
            mini = min(mini, dp(0, 0, target))
        return mini
