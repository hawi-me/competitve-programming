class FrequencyTracker:
    def __init__(self):
        self.dict = defaultdict(int)
        self.dict_freq= defaultdict(int)

    def add(self, number: int) -> None:

            self.dict_freq[self.dict[number]]-=1
            self.dict[number] += 1
            self.dict_freq[self.dict[number]]+=1

    def deleteOne(self, number: int) -> None:

        if self.dict_freq[self.dict[number]] > 0:
                self.dict_freq[self.dict[number]]-= 1
                self.dict[number] -=1
                self.dict_freq[self.dict[number]]+=1

    def hasFrequency(self, frequency: int) -> bool:
        if frequency in self.dict_freq and self.dict_freq[frequency] > 0:
            return True 
        return False


        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)