class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        result = []
        remaining = []
        count = {}

        for num in arr1:
            if num in arr2:
                if num in count:
                    count[num] += 1
                else:
                    count[num] = 1
            else:
                remaining.append(num)

        for num in arr2:
            if num in count:
                result.extend([num] * count[num])

        remaining.sort()
        result.extend(remaining)

        return result

