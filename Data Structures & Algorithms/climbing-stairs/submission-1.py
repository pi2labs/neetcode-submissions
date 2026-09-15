class Solution:
    def climbStairs(self, n: int) -> int:
        mp = [0] * (n+1)

        mp[0] = 1
        mp[1] = 1

        for i in range(2, n+1):
            mp[i] = mp[i-1] + mp[i-2]
        print(mp)
        return mp[-1]