class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        i = len(arr) - 1
        greatest = -1

        while i >= 0:
            cur_val = arr[i]
            arr[i] = greatest

            if cur_val > greatest:
                greatest = cur_val
            
            i -= 1
        
        return arr
        