from collections import Counter 
class Solution:
    def romanToInt(self, s: str) -> int:
        # Motham GPT help chesindhi 
        val={
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        sum=0
        for i in range(len(s)):
            if i+1<len(s) and  val[s[i]]<val[s[i+1]]:
                sum-=val[s[i]]
            else:
                sum+=val[s[i]]
        return sum
        
        