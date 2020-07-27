#0   0
#1  11
#2 2 2
#3   3

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1 or numRows==len(s):
            return s
        row, step = 0,0
        lst=['']*len(s)
        for i in s:
            lst[row]+=i
            if row==0:
                step=1
            elif row==numRows:
                step=-1
            row+=step
        return "".join(lst)

if __name__ == '__main__':
    result = Solution()
    print(result.convert('Paypal',4))
    print(result.convert('Hello',2))
