class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        #Took strivers help & GPT Help
        triangle=[[1]]
        for i in range(1,numRows):
            prev=triangle[-1]
            curr=[1]
            for j in range(1,len(prev)):
                curr.append(prev[j-1]+prev[j])
            curr.append(1)
            triangle.append(curr)
        return triangle