class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        map={}
        res=[-1]*len(nums1)
        for i in range(len(nums1)):
            map[nums1[i]] = i
        print(map)
        for j in range(len(nums2)):
            while stack and nums2[j] > stack[-1]:
                val=stack.pop()
                index=map[val]
                res[index] = nums2[j]
            if nums2[j] in map:
                stack.append(nums2[j])
        return res
                     


        