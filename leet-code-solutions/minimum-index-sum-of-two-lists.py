class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        res = []
        mapp = {}
        for i in range(len(list1)):
            mapp[list1[i]] = i
        min_sum = float("inf")
        for j in range(len(list2)):
            if list2[j] in mapp:
                total_index = j + mapp[list2[j]]
                if total_index < min_sum:
                    min_sum = total_index
                    res = [list2[j]]
                elif total_index == min_sum:
                    res.append(list2[j])
        return res

