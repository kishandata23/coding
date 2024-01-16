class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set_v=set(nums)
        return len(nums)!=len(set_v)
        