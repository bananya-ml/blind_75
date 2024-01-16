'''
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
'''


class Solution(object):
    def margeIntervals(self, intervals):
        '''
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        '''
        intervals.sort(key=lambda x: x[0])
        output = [intervals[0]]

        for start, end in intervals[1:]:
            lastEnd = output[-1][1]
            if start <= lastEnd:
                output[-1][1] = max(lastEnd, end)
            else:
                output.append([start, end])

        return output


intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(Solution().margeIntervals(intervals))
