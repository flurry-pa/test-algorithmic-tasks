"""  LeetCode
1482. Minimum Number of Days to Make m Bouquets
Medium
https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/
You are given an integer array bloomDay, an integer m and an integer k.
You want to make m bouquets.
To make a bouquet, you need to use k adjacent flowers from the garden.
The garden consists of n flowers, the ith flower will bloom in the bloomDay[i]
and then can be used in exactly one bouquet.
Return the minimum number of days you need to wait to be able to make m bouquets from the garden.
If it is impossible to make m bouquets return -1.
"""
from typing import List

TESTCASE = (
    ([1, 10, 3, 10, 2], 3, 1),
    ([1, 10, 3, 10, 2], 3, 2),
    ([7, 7, 7, 7, 12, 7, 7], 2, 3)
)
OUTPUTS = 3, -1, 12


class Solution1:
    def minDay(self, bloomDay: List[int], m: int, k: int) -> int:

        for bloom_day in sorted(set(bloomDay)):
            bouquet_qty = 0
            flowers_in_bouquet = 0

            for flower_day in bloomDay:

                if flower_day <= bloom_day:
                    flowers_in_bouquet += 1

                    if flowers_in_bouquet == k:
                        bouquet_qty += 1
                        flowers_in_bouquet = 0

                else:
                    flowers_in_bouquet = 0

            if bouquet_qty >= m:
                return bloom_day

        return -1


class Solution:
    def minDay(self, bloomDay: List[int], m: int, k: int) -> int:
        unic_bloom_days = sorted(set(bloomDay))
        unic_bloom_days.insert(0, 0)
        result = -1

        while True:
            bouquet_qty = 0
            flowers_in_bouquet = 0
            cur_bloom_day = unic_bloom_days[int(len(unic_bloom_days)/2)]

            for flower_day in bloomDay:

                if flower_day <= cur_bloom_day:
                    flowers_in_bouquet += 1

                    if flowers_in_bouquet == k:
                        bouquet_qty += 1
                        flowers_in_bouquet = 0

                else:
                    flowers_in_bouquet = 0

            ind = unic_bloom_days.index(cur_bloom_day)

            if bouquet_qty >= m:
                unic_bloom_days = unic_bloom_days[:ind + 1]
                result = cur_bloom_day

            else:
                unic_bloom_days = unic_bloom_days[ind:]

            if cur_bloom_day == unic_bloom_days[int(len(unic_bloom_days)/2)]:
                return result


solution = Solution()

for _, testcase in enumerate(TESTCASE):
    result = solution.minDay(
        bloomDay=testcase[0],
        m=testcase[1],
        k=testcase[2]
    )
    # print(f"result={result}")
    assert result == OUTPUTS[_], f"Testcase #{_ + 1}: output = {OUTPUTS[_]} expected, got: {result}"

print("Done.")

# Runtime 1233 ms Beats 80.2%,  Memory 32.4 MB Beats 5.80%
