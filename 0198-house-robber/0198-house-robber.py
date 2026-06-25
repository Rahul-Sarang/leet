class Solution(object):
    def rob(self, nums):
        dp = {}
        def helper(i):
            if i >= len(nums):
                return 0
            if i in dp:
                return dp[i]
            robCurrent = nums[i] + helper(i + 2)
            skipCurrent = helper(i + 1)
            dp[i] = max(robCurrent, skipCurrent)
            return dp[i]
        return helper(0)