class Solution:
    def checkValidString(self, s: str) -> bool:
        #GPT Helped with this approach
        low=0
        high=0
        for ch in s:
            if ch =="(":
                low+=1
                high+=1
            elif ch==")":
                low-=1
                high-=1
            else:
                low-=1
                high+=1
            low=max(0,low)
            if high<0:
                return False
        return low==0