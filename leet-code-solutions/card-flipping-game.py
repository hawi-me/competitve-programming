class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        invalid = set()
        output = []
        for i in range(len(fronts)):
            if fronts[i] == backs[i]:
                invalid.add(fronts[i])
        
        for i in range(len(fronts)):
            if fronts[i] not in invalid:
                output.append(fronts[i])
            if backs[i] not in invalid:
                output.append(backs[i])
        
        if not output:  # Check if the list is empty
            return 0
        else:
            return min(output)


