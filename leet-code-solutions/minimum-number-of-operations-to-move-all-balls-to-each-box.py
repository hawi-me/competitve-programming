class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        answer=[]
        for i in range(len(boxes)):
            total=0
            for j in range(len(boxes)):
                if(boxes[j]=='1'):
                    total+=abs(i-j)
            answer.append(total)

        return answer