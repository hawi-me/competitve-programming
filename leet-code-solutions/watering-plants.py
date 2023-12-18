class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        steps=0
        water=capacity
        for i, p in enumerate(plants):
            steps +=1
            if water >= p:
                water -= p
            else:
                steps += 2*i
                water= capacity -p
        return steps 