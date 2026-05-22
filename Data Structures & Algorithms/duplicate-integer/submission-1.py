class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sorted_array = set(nums)
        if len(sorted_array) < len(nums):
            return True
        return False