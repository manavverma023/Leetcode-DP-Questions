'''
************************************************

https://leetcode.com/problems/delete-and-earn/

***********************************************
'''

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        ma=max(nums)
        w=[0]*(ma+1)
        dp=[0]*(ma+1)
        if len(nums)==1:
            return nums[0]
        for i in nums:
            w[i]+=i
        
        for i in range(1,ma+1):
            if i==1:
                dp[i]=w[i]
            else:
                dp[i]=max(dp[i-1],dp[i-2]+w[i])
        #print(dp)
        return dp[-1]
