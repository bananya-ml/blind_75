'''
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.
'''


class Solution(object):
    def minMeetingRooms(self, intervals):
        '''
        :type intervals: List[List[int]]
        :rtype: int
        '''
        start = sorted([i[0] for i in intervals])
        end = sorted([i[1] for i in intervals])

        res = count = 0
        s = e = 0
        while s < len(intervals):
            if start[s] < end[e]:
                count += 1
                s += 1
            else:
                count -= 1
                e += 1
            res = max(res, count)
        return res


intervals = [(0, 30), (5, 10), (15, 20)]
print(Solution().minMeetingRooms(intervals))
