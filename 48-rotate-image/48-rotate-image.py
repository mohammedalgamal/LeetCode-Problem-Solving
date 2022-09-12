class Solution(object):
    def rotate(self, x):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(x)
        
        for i in range(n):
            x.append([])   
            
        for i in range(n - 1, -1, -1):
            for j in range(n):
                x[n + j].append(x[i][j])
                
        del x[:n]        