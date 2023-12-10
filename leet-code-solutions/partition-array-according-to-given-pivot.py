class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        greater=[]
        lesser=[]
        count=nums.count(pivot)
        pivotes=[pivot]*count
        for i in range(len(nums)):
            if nums[i] < pivot:
                lesser.append(nums[i])
            if nums[i] > pivot:
                greater.append(nums[i])
        lesser.extend(pivotes + greater)
        return lesser

