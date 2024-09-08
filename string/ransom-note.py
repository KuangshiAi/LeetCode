class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        dictionary = {}
        for char in magazine:
            if char not in dictionary:
                dictionary[char] = 1
            else:
                dictionary[char] += 1
        
        for char in ransomNote:
            if char in dictionary:
                dictionary[char] -= 1
                if dictionary[char] == 0:
                    dictionary.pop(char)
            else:
                return False
        
        return True