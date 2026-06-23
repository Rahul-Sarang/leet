class Solution:
    def missingNumber(self, nums: List[int]) -> int:
       n=len(nums)
       ETS=(n*(n+1))//2
       ATS=sum(nums)
       return ETS-ATS