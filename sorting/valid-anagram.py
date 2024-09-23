class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        mydict = {}
        for char in s:
            if char in mydict.keys():
                mydict[char] += 1
            else:
                mydict[char] = 1
        for char in t:
            if char in mydict.keys():
                mydict[char] -= 1
                if mydict[char] == 0:
                    del mydict[char]
            else:
                return False
        if not mydict:
            return True