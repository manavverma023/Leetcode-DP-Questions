'''
************************************************

https://leetcode.com/problems/climbing-stairs/

************************************************
'''

class Solution:
    def climbStairs(self, n: int) -> int:
        ans=0
        n1=0
        n2=1
        count=0
        while count < n+2:
            ans=n1
            nth = n1 + n2
            n1 = n2
            n2 = nth
            count += 1
        return ans
        
        
