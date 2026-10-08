class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        #Karthik Helped
        o=0
        c=0
        ans=""
        l=0
        for r in range(len(s)):
            if s[r]=="(":
                o+=1
            else:
                c+=1
            if o==c:
                ans+=s[l+1:r]
                l=r+1
        return ans

        