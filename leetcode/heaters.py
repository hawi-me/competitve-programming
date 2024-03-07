class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        houses.sort()
        def checker(mid):
            i=0
            j = 0
            while i < len(houses):
                x = heaters[j] - mid  
                y = heaters[j] + mid 
                if houses[i]  >= x and  houses[i] <= y:
                    i += 1
                else:
                    j += 1
                if j >= len(heaters):
                    return False  
            return True

        l = 0
        m1 = max(heaters)
        m2 = max(houses)
        h = max(m1, m2)
        while l <= h:
            mid = (l + h) // 2
            if checker(mid):
                h = mid - 1
            else:
                l = mid + 1        
        return l
