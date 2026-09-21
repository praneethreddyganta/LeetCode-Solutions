class Solution:
    def fib(self, n: int) -> int:
        if n==0:
            return 0
        elif n==1:
            return 1
        elif n==2:
            return 1
        a=1
        b=1
        for i in range(3,n+1):
            curr=a+b
            a=b
            b=curr
        return curr