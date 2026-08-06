class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        for i in range(t):
            prod=1
            temp=n
            while temp>0:
                r=temp%10
                temp=temp//10
                prod*=r
            if prod%t==0:
                return n
            n+=1