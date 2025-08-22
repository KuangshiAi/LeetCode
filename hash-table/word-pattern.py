class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        words = s.split(' ')
        hashmap = {}
        for i in range(len(pattern)):
            char = pattern[i]
            if char not in hashmap.keys() and words[i] not in hashmap.values():
                hashmap[char] = words[i]
            elif words[i] != hashmap[char]:
                return False
        return True
                
        