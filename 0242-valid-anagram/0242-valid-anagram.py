class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq1={}
        for val in s:
            freq1[val]=freq1.get(val,0)+1
        freq2={}
        for val in t:
            freq2[val]=freq2.get(val,0)+1
        return True if freq1==freq2 else False
        