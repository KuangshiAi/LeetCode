import random
class RandomizedSet(object):

    def __init__(self):
        self.pos = {}
        self.arr = []

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.pos.keys():
            return False
        self.pos[val] = len(self.arr)
        self.arr.append(val)
        return True
        

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.pos.keys():
            return False
        last = self.arr[-1]
        i = self.pos[val]
        self.arr[i] = last
        self.pos[last] = i
        self.arr.pop()
        return True
        

    def getRandom(self):
        """
        :rtype: int
        """
        return self.arr[random.randrange(len(self.arr))]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()