class Solution:
    def checkString(self, s: str) -> bool:
        #Motham Gpt ney nenem cheyyaley
        '''
        if "ba" in s:
            return False
        return True
        '''
        found_b=False
        for ch in s:
            if ch=="b":
                found_b=True
            if ch=="a" and found_b==True:
                return False
        return True

        