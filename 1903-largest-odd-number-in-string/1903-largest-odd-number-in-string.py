class Solution:
    def largestOddNumber(self, num: str) -> str:
        # Took Strivers help
        l=-1
        for i in range(len(num)-1,-1,-1):
            if int(num[i])%2!=0:
                l=i
                break
        if l==-1:
            return ""
        for j in range(len(num)):
            if num[j]!='0':
                s=j
                break
        return num[s:l+1]