import random

class RandomizedSet:

    def __init__(self):
        self.mylist = []
        self.mydict = {}

    def insert(self, val: int) -> bool:
        if val not in self.mydict:
            self.mylist.append(val)
            self.mydict[val] = len(self.mylist) - 1
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.mydict:
            index = self.mydict[val]
            last_val = self.mylist[-1]
            self.mylist[index] = last_val
            self.mydict[last_val] = index
            self.mylist.pop()
            del self.mydict[val]
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.mylist)