class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Motham GPT Help chesindhi
        count=0
        for  chr in reversed(s):
            if chr==" ":
                if count>0:
                    break
            else:
                count+=1
        return count
