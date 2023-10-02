"""  LeetCode. Akvelon interview
42. Trapping Rain Water
Hard
https://leetcode.com/problems/trapping-rain-water/description/
Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it can trap after raining.
"""
from typing import List

TESTCASE = (
    [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1],
    [4, 2, 0, 3, 2, 5]
)
OUTPUTS = 6, 9


class Solution:
    def trap(self, height: List[int]) -> int:
        vol = 0

        if len(height) < 3:
            return vol

        left_max = height[0]
        right_max = max(height[2:])

        for j in range(1, len(height) - 1):

            if left_max < height[j - 1]:
                left_max = max(height[:j])

            if right_max == height[j]:
                right_max = max(height[j + 1:])

            level = min(left_max, right_max)

            if height[j] < level:
                vol += level - height[j]

        return vol


solution = Solution()

for _, testcase in enumerate(TESTCASE):
    result = solution.trap(height=testcase)
    # print(f"result={result}")
    assert result == OUTPUTS[_], f"Testcase #{_ + 1}: output = {OUTPUTS[_]} expected, got: {result}"

print("Done.")
