'''
*******************************************************

https://leetcode.com/problems/n-th-tribonacci-number/

******************************************************
'''

class Solution:
    def tribonacci(self, n: int) -> int:
        f=[0,1,1]
        if n==0:
            return 0
        elif n==1:
            return 1
        elif n==2:
            return 1
        else:
            for i in range(3,n+1):
                s=f[i-1]+f[i-2]+f[i-3]
                f.append(s)
            return f[-1]
