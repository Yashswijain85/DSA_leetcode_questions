class Solution:
    def merge(self, intervals):
        n = len(intervals)

        # sort based on starting point 
        intervals.sort(key = lambda i : i[0])

        result = [intervals[0]]

        for start, end in intervals[1:]:
            previousIntervalEnd = result[-1][1]
            if start <= previousIntervalEnd:
                result[-1][1] = max(previousIntervalEnd, end)
            else:
                result.append([start, end])
        return result 
