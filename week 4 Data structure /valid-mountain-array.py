class Solution:
    def validMountainArray(self, arr):
        n = len(arr)
        strat, end = 0, n - 1
        while strat != n-1 and arr[strat + 1] > arr[strat]: strat += 1
        while end != 0 and arr[end - 1] > arr[end]: end -= 1 
        return strat == end and end != n-1 and strat != 0


      


            
