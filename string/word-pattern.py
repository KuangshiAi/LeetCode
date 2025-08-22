class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        words = s.split(' ')
        hashmap = {}
        if len(words) != len(pattern):
            return False
        for i in range(len(pattern)):
            char = pattern[i]
            if char not in hashmap.keys() and words[i] not in hashmap.values():
                hashmap[char] = words[i]
            elif char not in hashmap.keys() or words[i] != hashmap[char]:
                return False
        return True
                
        