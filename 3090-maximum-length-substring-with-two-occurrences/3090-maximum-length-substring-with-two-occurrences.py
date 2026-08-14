class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        n=len(s)
        #GPT Helped with window_length 
        freq={}
        l=0
        max_count=0
        for r in range(n):
            if s[r] not in freq:
                freq[s[r]]=1
                
            else:
                freq[s[r]]+=1
                
            
            while freq[s[r]]>2:
                freq[s[l]]-=1
                l+=1
            window_length=r-l+1
            max_count=max(max_count,window_length)
            
        return max_count
