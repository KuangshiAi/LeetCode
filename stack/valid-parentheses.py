class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        from collections import deque
        stack = deque()
        bracket_map = {')':'(', '}':'{', ']':'['}
        for char in s:
            if char in bracket_map.values():
                stack.append(char)
            elif not stack or bracket_map[char] != stack.pop():
                return False
        if stack:
            return False
        return True