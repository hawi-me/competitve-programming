from typing import List

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        eachbill = 0
        total_5 = 0
        total_10 = 0
        
        for bill in bills:
            if bill == 5:
                total_5 += 1
            elif bill == 10:
                if total_5 >= 1:
                    total_5 -= 1
                    total_10 += 1
                else:
                    return False
            elif bill == 20:
                if total_10 >= 1 and total_5 >= 1:
                    total_10 -= 1
                    total_5 -= 1
                elif total_5 >= 3:
                    total_5 -= 3
                else:
                    return False
        
        return True
