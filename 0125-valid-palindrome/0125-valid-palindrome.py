class Solution:
    import re
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        s1=re.sub(r'[^a-zA-Z0-9]','',s)
        s2=list(s1)
        temp=s2.copy()
        left=0
        right=len(s2)-1
        while left<right:
            s2[left],s2[right]=s2[right],s2[left]
            left+=1
            right-=1
        return True if s2==temp else  False