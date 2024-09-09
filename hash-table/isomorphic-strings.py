class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        idxs = {}
        idxt = {}
        for i in range(len(s)):
            if s[i] not in idxs:
                idxs[s[i]] = i
            if t[i] not in idxt:
                idxt[t[i]] = i
            if idxs[s[i]] != idxt[t[i]]:
                return False
            idxs[s[i]] = i
            idxt[t[i]] = i
        
        return True
        