"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals = sorted(intervals, key = lambda i: i.start)       
        if not intervals: return True

        for i in range(1, len(intervals)):
            st = intervals[i].start
            ed = intervals[i].end



            if st < intervals[i-1].end:
                return False
        
        
        return True
            
