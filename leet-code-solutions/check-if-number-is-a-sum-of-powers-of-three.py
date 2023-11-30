class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        
          while n:
             while not n % 3:
                 n //= 3
             if n % 3 == 2: return False
             n -=n % 3
          return True


            

           
           

