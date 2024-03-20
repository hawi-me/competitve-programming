class Solution:
    def numberOfWays(self, s: str) -> int:
        count0 , count1 = 0 , 0
        count0_right = s.count('0')
        count1_right = s.count('1')
        valid_way = 0
        for build  in s:
            if build == '1':
                valid_way += count0*count0_right
                count1 += 1
                count1_right -= 1
            else:
                valid_way += count1*count1_right
                count0 += 1
                count0_right -= 1
        return valid_way        