class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
       maxi= max(start,destination)
       minimum = min(start,destination)
       s1= sum(distance[minimum:maxi])
       s2= sum(distance[:minimum]) + sum(distance[maxi:])
       return min(s1,s2)