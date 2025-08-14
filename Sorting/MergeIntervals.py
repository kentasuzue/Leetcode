"""
56. Merge Intervals
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping. 

Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104
"""

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort beginnings
        # [1, 2, 8, 15]
        # dict maps each beginning to an end 
        # if multiple intervals have same beginning, throw away smaller ending
        # iterate through sorted beginnings, store largest ending
        # if ending of any prior interval >= beginning of next interval,
        # then merge intervals
        if len(intervals) == 1:
            return intervals

        intervalBegins = []
        intervalDict = {}
        for intervalBegin, intervalEnd in intervals:
            if intervalBegin not in intervalDict:
                intervalBegins.append(intervalBegin)
                intervalDict[intervalBegin] = intervalEnd
            elif intervalEnd > intervalDict[intervalBegin]:
                intervalDict[intervalBegin] = intervalEnd
        
        intervalBegins = sorted(intervalBegins)
        # print(intervalBegins)
        # print(intervalDict)
        priorInterval = [intervalBegins[0], intervalDict[intervalBegins[0]]]
        # print(priorInterval)

        for i in range(1,len(intervalBegins)):
            # if prior interval and current interval overlap, merge intervals
            if priorInterval[1] >= intervalBegins[i]:
                # print(f"intervalBegins[i] = {intervalBegins[i]}")
                # print(f"priorInterval[0] = {priorInterval[0]}, intervalDict[intervalBegins[i]] = {intervalDict[intervalBegins[i]]}")
                # update prior interval
                intervalDict[priorInterval[0]] = max(priorInterval[1], intervalDict[intervalBegins[i]])
                priorInterval[1] = intervalDict[priorInterval[0]]
                # delete current interval from intervalDict
                if not (intervalBegins[i] == priorInterval[0]):
                    del(intervalDict[intervalBegins[i]])
            # update prior interval
            else:
                priorInterval = [intervalBegins[i], intervalDict[intervalBegins[i]]]
        
        answer = []

        # print(intervalDict)

        for key, value in intervalDict.items():
            answer.append([key, value])
        return answer


            


