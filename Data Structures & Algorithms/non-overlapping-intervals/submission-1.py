class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda i:i[0])
        #print(intervals)
        output = [intervals[0]]
        print(output)
        res = 0
        for start, end in intervals[1:]:
            lastEnd = output[-1][1]
            print("start: ", start, "end: ", end, "lastEnd: ", lastEnd)
            if start < lastEnd:
                output[-1][1] = min(lastEnd, end)
                #print("length of output: ", len(output), "length of intervals: ", len(intervals))
                res += 1
                print("updates res: ", res, "updated output: ", output)
            else:
                output.append([start,end])
        return res



