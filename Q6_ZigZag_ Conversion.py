#0   0
#1  11
#2 2 2
#3   3

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        
        row, step = 0, 0
        res = [''] * len(s)
        
        for c in s:
            print(res,row)
            res[row] += c
            
            if row == 0:
                step = 1
            elif row == numRows - 1:
                step = -1
                
            row += step
        
        return "".join(res)
