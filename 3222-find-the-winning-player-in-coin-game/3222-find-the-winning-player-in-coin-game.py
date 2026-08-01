class Solution:
    def winningPlayer(self, x: int, y: int) -> str:
        result=min(x,y//4)
        #Took Help from hints
        if result%2==0:
            return "Bob"
        else:
            return "Alice"
        