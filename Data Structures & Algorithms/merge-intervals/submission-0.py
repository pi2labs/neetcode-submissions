class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []

        intervals = sorted(intervals, key=lambda x: x[0])

        print(intervals)

        res = []

        s = intervals[0][0]
        e = intervals[0][1]

        for i in range(1, len(intervals)):

            st = intervals[i][0]
            et = intervals[i][1]

            if st <= e:
                e = max(e, et)
                continue
            else:
                res.append([s, e])
                s = st
                e = et
                
        res.append([s, e])   
        return res

