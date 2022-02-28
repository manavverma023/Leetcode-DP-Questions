'''
***************************************************

https://leetcode.com/problems/house-robber-ii/
  
***************************************************
'''

class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0],self.hr(nums[1:]),self.hr(nums[:-1]))
    
    def hr(self,nums):
        r1=0
        r2=0
        for i in nums:
            t=max(r1+i,r2)
            r1=r2
            r2=t
        return r2
