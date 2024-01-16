'''
Given an array of meeting time intervals intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required. 
'''


class Solution(object):
    def canAttendMeetings(self, intervals):
        '''
        :type intervals: List[List[int]]
        :rtype: int
        '''
        intervals.sort(key=lambda x: x.start)

        for i in range(1, len(intervals)):
            i1 = intervals[i-1]
            i2 = intervals[i]
            if i1.end > i2.start:
                return False
        return True


intervals = [[0, 30], [5, 10], [15, 20]]
print(Solution().meetingRooms(intervals))
