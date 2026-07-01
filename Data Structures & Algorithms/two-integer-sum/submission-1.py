class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indeces = {}

        for i, n, in enumerate(nums):
            indeces[n] = i

        for i, n, in enumerate(nums):
            diff = target-n
            if diff in indeces and indeces[diff]!=i:
                return [i, indeces[diff]]
        return []