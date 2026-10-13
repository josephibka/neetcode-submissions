class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        score = 0
        for i in range(0,len(nums)):
            if nums[i] != val:
                nums[score] = nums[i]
                score += 1
        return score

