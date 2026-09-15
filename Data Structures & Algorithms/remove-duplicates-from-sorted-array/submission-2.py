class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        x = 1

        for y in range(1,len(nums)):
            if nums[y-1] != nums[y]:
                nums[x] = nums[y]
                x += 1
        
        return x