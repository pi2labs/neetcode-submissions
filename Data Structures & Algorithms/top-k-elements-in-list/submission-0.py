class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        mp = collections.Counter(nums)

        mp_new = {}
        for key,value in mp.items():
            if value not in mp_new:
                mp_new[value] = [key]
            else:
                mp_new[value].append(key)

        res = []

        keys_sorted = sorted(mp_new.keys(), reverse=True)

        for key in keys_sorted:
            for j in mp_new[key]:
                k -= 1
                res.append(j)
                if k == 0:
                    break
            if k == 0:
                break

        return res