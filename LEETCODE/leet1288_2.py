class Solution(object):
    def removeCoveredIntervals(self, intervals):
        intervals.sort(key = lambda x:(x[0], -x[1]))

        cnt = 0
        end = 0

        for a, b in intervals:
            if b > end:
                cnt += 1
                end = b
        return cnt

# in this way we sorted first, so c<=a condition of leet 1288 is correct as we move on, 
# now we only wait for b<=d condition and if that gets true then element isnt counted

