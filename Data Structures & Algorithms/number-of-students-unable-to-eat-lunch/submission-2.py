class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        res = len(sandwiches)

        mp = {0: 0, 1:0}

        for i in students:
            mp[i] += 1

        for j in sandwiches:
            if mp[j] > 0:
                mp[j] = mp[j] - 1
                res = res - 1
            else:
                break
        return res



