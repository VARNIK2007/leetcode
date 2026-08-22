class Solution:
    def checkDivisibility(self, n: int) -> bool:
        s=0
        p=1
        v=n
        while n:
            r=n%10
            s=s+r
            p=p*r
            n=n//10
        
        if(v%(s+p)==0):
            return True
        else:
            return False
        