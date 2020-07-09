# find the longest palindromic substring 

class Solution:
    def longestPalindrome(self, s: str) -> str:
        l = len(s)
        m=''
        if l<2:
            return s 
        else:
            for i in range(len(s)):
                for j in range(len(s), i, -1):
                    if len(m)>= j-i:
                        break
                    elif s[i:j]==s[i:j][::-1]:
                        m = s[i:j]
                        break
            return m
