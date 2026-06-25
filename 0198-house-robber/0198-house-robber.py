class Solution:
    def rob(self, nums: List[int]) -> int:
        x = 0
        y = 0
        i = 0
        while i < len(nums):
            current = max(x, y+ nums[i])
            y = x
            x = current
            i += 1
        return x