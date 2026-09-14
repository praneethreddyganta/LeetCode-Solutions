class Solution:
    def isValid(self, s: str) -> bool:
        #Motham gpt help ey thiskunna
        stack=[]
        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        for ch in s:
            if ch in "([{":
                stack.append(ch)
            else:
                if not stack or stack[-1]!=pairs[ch]:
                    return False
                stack.pop()
        return len(stack)==0
