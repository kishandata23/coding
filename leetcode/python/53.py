class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum=nums[0]
        currentSum=nums[0]
        for num in nums[1:]:
            currentSum=max(num,currentSum+num)
            max_sum=max(currentSum,max_sum)
        return max_sum
        