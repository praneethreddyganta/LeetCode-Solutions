class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp=x
        sum=0
        while temp>0:
            r=temp%10
            sum=sum*10+r
            temp=temp//10
        return True if x==sum else False
        