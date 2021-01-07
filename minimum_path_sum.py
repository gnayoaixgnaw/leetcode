class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        temp = [[0 for i in range(len(grid[0]))]for i in range(len(grid))]
        temp[0][0] = grid[0][0]
        
        for i in range(1,len(grid[0])):
            temp[0][i] = grid[0][i] + temp[0][i-1]
            
        for j in range(1,len(grid)):
            temp[j][0] = grid[j][0] + temp[j-1][0]
            
        
        for i in range(1,len(grid[0])):
            for j in range(1,len(grid)):
                temp[j][i] = grid[j][i] + min(temp[j-1][i],temp[j][i-1])
        
        return temp[len(grid)-1][len(grid[0])-1]
