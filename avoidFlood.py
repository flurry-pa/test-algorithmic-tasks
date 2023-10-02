"""  LeetCode
1488. Avoid Flood in The City
Medium
https://leetcode.com/problems/avoid-flood-in-the-city/
Your country has an infinite number of lakes.
Initially, all the lakes are empty, but when it rains over the nth lake,
the nth lake becomes full of water.
If it rains over a lake that is full of water, there will be a flood.
Your goal is to avoid floods in any lake.

Given an integer array rains where:
rains[i] > 0 means there will be rains over the rains[i] lake.
rains[i] == 0 means there are no rains this day, and you can choose one lake this day and dry it.

Return an array 'ans' where:
ans.length == rains.length
ans[i] == -1 if rains[i] > 0.
ans[i] is the lake you choose to dry in the ith day if rains[i] == 0.
If there are multiple valid answers return any of them. If it is impossible to avoid flood return an empty array.

Notice that if you chose to dry a full lake, it becomes empty,
but if you chose to dry an empty lake, nothing changes.
"""
from typing import List, Optional
from collections import deque
import bisect

TESTCASE = (
    [1, 2, 3, 4],
    [1, 2, 0, 2, 0, 1],
    [1, 2, 0, 1, 2],
    [1, 0, 2, 0],
    [1, 0, 2, 0, 2, 1],
    [1, 1, 0, 0],
    [1, 0, 2, 3, 0, 1, 2],
    [1, 2, 0, 1, 0, 2],
    [1, 0, 2, 0, 3, 0, 2, 0, 0, 0, 1, 2, 3],
)
OUTPUTS = (
    [-1, -1, -1, -1],
    [-1, -1, 2, -1, 1, -1],
    [],
    [-1, 1, -1, 1],
    [-1, 1, -1, 2, -1, -1],
    [],
    [-1, 1, -1, -1, 2, -1, -1],
    [-1, -1, 1, -1, 2, -1],
    [-1, 1, -1, 2, -1, 3, -1, 2, 1, 1, -1, -1, -1]
)


def find_gt(lst: List[int], val: int) -> Optional[int]:
    """ Find leftmost value greater than val """
    i = bisect.bisect_left(lst, val)
    if i != len(lst):
        return lst[i]
    return None


class MySolution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        dry_days = list()    # days to dry any lake
        full_lakes = dict()  # {rain: day_index}
        ans = list()

        for i_day, rain in enumerate(rains):

            if rain == 0:
                dry_days.append(i_day)
                ans.append(1)

            elif rain in full_lakes:
                # print(f"({dry_days}, {full_lakes[rain]})")
                dry_day = find_gt(lst=dry_days, val=full_lakes[rain])
                # dry_day = bysearch_gt(lst=dry_days, val=full_lakes[rain])

                if not dry_day:
                    return []

                full_lakes.update({rain: i_day})
                dry_days.remove(dry_day)
                ans[dry_day] = rain
                ans.append(-1)

            else:
                full_lakes.update({rain: i_day})
                ans.append(-1)

        return ans

# My solutions:
# Compare 3 methods to find lake to dry (binary search) for this solution
# Runtime 1237 ms Beats 16.99%          Memory 31.5 MB Beats 77.67%     bisect.bisect_right
# Runtime 1215 ms Beats 21.85%          Memory 31.6 MB Beats 77.67%     bisect.bisect_left
# Runtime 1222 ms Beats 20.39%          Memory 34.4 MB Beats 39.32%     bysearch_gt


class BestSolution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        dry_days = deque()   # days to dry any lake
        full_lakes = dict()  # {rain: day_index}
        ans = [-1] * len(rains)

        for i_day, rain in enumerate(rains):

            if rain == 0:
                dry_days.append(i_day)
                ans[i_day] = 1

            elif rain in full_lakes:

                for day in dry_days:

                    if day > full_lakes[rain]:
                        full_lakes.update({rain: i_day})
                        dry_days.remove(day)
                        ans[day] = rain
                        break
                else:
                    return []

            else:
                full_lakes.update({rain: i_day})

        return ans
# Idea from the best solution: dry_days = deque() (ie, Linked List, not list()!!!).
# Execution time decrease here: "dry_days.remove(day)"
# Code the same as my Solution3
# The best solution: Runtime 908 ms  Beats 100%        Memory  34.5 MB   Beats  39.71%


solution = MySolution()
# solution = BestSolution()

for k, testcase in enumerate(TESTCASE):
    result = solution.avoidFlood(rains=testcase)
    # print(f"result={result}")
    assert result == OUTPUTS[k], f"Testcase #{k + 1}: output = {OUTPUTS[k]} expected, got: {result}"

print("Done.")
