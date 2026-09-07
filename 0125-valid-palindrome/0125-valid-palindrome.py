class Solution:
    import re
    def isPalindrome(self, s: str) -> bool:
        # My Code 
        #Time and space:O(N)
        ''' s=s.lower()
        s1=re.sub(r'[^a-zA-Z0-9]','',s)
        s2=list(s1)
        temp=s2.copy()
        left=0
        right=len(s2)-1
        while left<right:
            s2[left],s2[right]=s2[right],s2[left]
            left+=1
            right-=1
        return True if s2==temp else  False'''
        #Gemini Optimsed 
        #Time:O(n) and space O(1)
        left=0
        right=len(s)-1
        while left<right:
            while left<right and  not s[left].isalnum():
                left+=1
            while left<right and not s[right].isalnum():
                right-=1
            if s[left].lower()!=s[right].lower():
                return False
            left+=1
            right-=1
        return True