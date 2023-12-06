class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
          ans=[]
          arr1=nums[0:n]
          arr2=nums[n:len(nums)]
          print(arr1)
          print(arr2)
          for i in range(len(arr1)):
              ans.append(arr1[i])
              ans.append(arr2[i])
          return  ans
        
                