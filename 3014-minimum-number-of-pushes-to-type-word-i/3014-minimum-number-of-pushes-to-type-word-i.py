class Solution:
    def minimumPushes(self, word: str) -> int:
        k=8
        c=0
        for i in range(len(word)):
            if k>0:
                c+=1
            
            elif k>-8 :
                c+=2
            
            elif k>-16:
                c+=3
            
            else:
                c+=4
            k-=1
        return c
            


        