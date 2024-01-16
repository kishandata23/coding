class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre_list =[1]*len(nums)
        post_list =[1]*len(nums)
        for i in range(len(nums)-1):
            pre_list[i+1]=nums[i]*pre_list[i]
        for i in range(len(nums)-1):
            i=-i-1
            post_list[i-1]=nums[i]*post_list[i]
        return [a*b for a,b in zip(pre_list,post_list)]
        