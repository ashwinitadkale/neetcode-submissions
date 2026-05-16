class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        cnt=0
        nums_set=set(nums)
        if len(nums_set)==len(nums):
            return False
        else:
            return True
        
        