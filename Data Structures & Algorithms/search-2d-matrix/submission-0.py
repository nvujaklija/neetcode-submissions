class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def search(nums, target):
            l, r = 0, len(nums)-1
            while l<=r:
                mid = int((l+r)/2)
                if nums[mid]==target:
                    return True
                elif nums[mid]<target:
                    l = mid+1
                else:
                    r = mid-1
            return False
        l, r = 0, len(matrix)-1
        while l<=r:
            mid = int((l+r)/2)
            if target in matrix[mid]:
                return search(matrix[mid], target)
            elif matrix[mid][-1]<target:
                l = mid+1
            else:
                r = mid-1
        return False