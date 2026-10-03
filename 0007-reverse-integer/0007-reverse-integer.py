class Solution:
    def reverse(self, x: int) -> int:
        # GPT Helped with reversing a negative integer and 
        #[-231, 231 - 1] case 
        sign=1 if x>0 else -1
        x=abs(x)
        rev=0

        while x>0 :
            rev=rev*10+x%10
            x=x//10
        rev=rev*sign
        if rev <= -2**31 or  rev>=2**31-1:
            return 0
        return rev