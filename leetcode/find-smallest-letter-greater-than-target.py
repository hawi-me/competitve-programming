class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        n= bisect_right(letters, target) 
        return letters[n] if n <  len(letters) else letters[0]