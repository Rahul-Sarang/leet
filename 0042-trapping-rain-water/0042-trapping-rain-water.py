class Solution:
    def trap(self, height: List[int]) -> int:
        i=0
        j=len(height)-1
        leftM=0
        rightM=0
        water=0
        while i<j :
            if height[i]<height[j]:
                leftM=max(leftM,height[i])
                if height[i]<leftM:
                    water+=leftM-height[i]
                i+=1
            else:
                rightM=max(rightM,height[j])
                if height[j]<rightM:
                    water+=rightM-height[j]
                j-=1
        return water
