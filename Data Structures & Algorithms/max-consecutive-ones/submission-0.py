class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ones = 0
        val = 0

        for i in nums:
            if i == 1:
                val = val + 1
            else:
                val = 0
                
            if val > ones:
                ones = val
        return ones