'''
**************************************************

https://leetcode.com/problems/fibonacci-number/

**************************************************
'''

class Solution:
    def fib(self, n: int) -> int:
        f=[0,1]
        if n==0:
            return 0
        elif n==1:
            return 1
        else:
            for i in range(2,n+1):
                s=f[i-1]+f[i-2]
                f.append(s)
            return f[-1]
                
