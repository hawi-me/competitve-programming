class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in range(len(image)):
            image[i] = image[i][::-1]  
            for j in range(len(image[i])):
                image[i][j] = 1 - image[i][j]  
        return image

