class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        n=len(s)
        max_count=0
        for i in range(n):
            count=0
            freq={}
            for j in range(i,n):
                if s[j] not in freq:
                    freq[s[j]]=1
                    count+=1
                else:
                    freq[s[j]]+=1
                    if freq[s[j]]<=2:
                        count+=1
                    else:
                        break               
            max_count=max(max_count,count)
        return max_count
