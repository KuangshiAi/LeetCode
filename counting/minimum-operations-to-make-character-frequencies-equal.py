class Solution(object):
    def makeStringGood(self, s):
        """
        :type s: str
        :rtype: int
        """
        count=[0]*26
        for c in s:
            count[ord(c)-ord("a")] += 1
        
        def dp(i, deleted, target):
            if i == 26:
                return 0
            x = count[i]
            if x == target or x == 0:
                return dp(i+1, 0, target)
            if x > target:
                return dp(i+1, x-target, target) + x - target
            else:
                need = target - x
                insert = dp(i+1, 0, target) + need
                delete = dp(i+1, x, target) + x
                # if i-1 has deletion, then we can benefit from it for changing, min(#move(i-1), #move(i)) could be saved
                change = dp(i+1, 0, target) + need - min(deleted, need)
                return min(insert, delete, change)
        
        return min(dp(0,0,target) for target in range(max(count)+1))

        