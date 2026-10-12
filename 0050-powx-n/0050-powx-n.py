class Solution:
    def myPow(self, x: float, n: int) -> float:
        #GPT Helped
        ans=1.0
        negative=n<0
        n=abs(n)
        while n>0:
            if n%2==1:
                ans*=x
            x*=x
            n=n//2
        return 1/ans if negative else ans
        