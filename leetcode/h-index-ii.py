class Solution:
    def hIndex(self, citations: List[int]) -> int:
        l = 0
        h = len(citations) - 1
        while l <= h:
            mid = (l + h) // 2
            if citations[mid] < len(citations) - mid:
                l = mid + 1
            else:
                h = mid - 1
        return len(citations) - l
