class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        sum = 0
        min = salary[0]
        max= salary[-1]
        for i in salary:
            sum += i
        leng = len(salary)-2
        return float((sum - min-max) / leng)