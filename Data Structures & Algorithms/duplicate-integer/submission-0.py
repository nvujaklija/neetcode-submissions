class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        tupList = set(nums)
        if len(tupList)!= len(nums):
            return True
        else:
            return False