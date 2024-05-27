## Time complexity --> O(logn)
class Solution:
    def myPow(self, x: float, n: int) -> float:
        # base case condition
        if n == 0:
            return 1
        # base case condition
        elif n == 1:
            return x
        # if n is negative 
        elif n < 0:
            x = 1/x # take the reciprocal of x 
            n = -n # make n positive 
            result = self.myPow(x,n)
            return result 
        # if n is positive > 1
        else:
            mid = n//2
            result = self.myPow(x,mid)
            finalresult = result*result 
            if n % 2 == 0:
                return finalresult
            else:
                return x * finalresult 

