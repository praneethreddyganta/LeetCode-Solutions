class Solution:
    def processStr(self, s: str) -> str:
        string=''
        for i in range(len(s)):
            if s[i].islower():
                string+=(s[i])
            elif s[i]=='*':
                if string:
                    string=string[:-1]
            elif s[i]=='#':
                string+=string
            else:
                string=string[::-1]
        return string
