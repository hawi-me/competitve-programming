class Solution:
    def bestClosingTime(self, customers: str) -> int:
        prefix_y = [0] * (len(customers) + 1)
        prefix_N = [0] * (len(customers) + 1)
        for i in range(len(customers) - 1, -1, -1):
            prefix_y[i] = prefix_y[i + 1]
            if customers[i] == "Y":
                prefix_y[i] += 1
        for i in range(1, len(customers) + 1):
            prefix_N[i] = prefix_N[i - 1]
            if customers[i - 1] == "N":
                prefix_N[i] += 1
        min_penalty, indx = float('inf'), 0
        for i in range(len(customers) + 1): 
            penalty = prefix_y[i] + prefix_N[i]
            if penalty < min_penalty:
                min_penalty = penalty
                indx = i
        return indx
