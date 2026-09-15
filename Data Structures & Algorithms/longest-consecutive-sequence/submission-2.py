class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums_set = set(nums)

        min_n = float('inf')
        res = 0
        starting_index_arr = []

        for i in nums_set:
            if (i - 1) not in nums_set:
                starting_index_arr.append(i)
        print(starting_index_arr)
        cnt = 0

        for j in starting_index_arr:
            
            isPresent = True
            starting_num = j
            while isPresent:
                if starting_num in nums_set:
                    cnt += 1
                else:
                    res = max(cnt, res)
                    isPresent = False
                    cnt = 0
                starting_num += 1
               

        return res

