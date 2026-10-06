class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        res = -1

        i = 0
        j = len(nums)

        while i < j:
            
            mid = (i + j) // 2
            if nums[mid] == target:
                return mid
            
            if nums[mid] < target:
                i += 1
            else:
                j -= 1
        
        return -1
            
