"""
Binary search algorithm.
Find a value from the list that is greater than a given value
case 1 - Python library
case 2 - my code
"""
from typing import List, Optional
import bisect

TESTCASE = (
    [[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21], 1],
    [[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21], 2],
    [[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21], 20],
    [[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21], 21],
    [[], 0],
    [[0], 0],
    [[0], 1],
    [[1], 0],
    [[1, 3], 2],
    [[1, 4], 0],
    [[5, 7, 8, 9], 9],
    [[5, 8, 9], 4],
    [[5, 5, 5, 8, 8, 8, 9], 7]
)
OUTPUTS = 3, 3, 21, None, None, None, None, 1, 3, 1, None, 5, 8


def find_gt(lst: List[int], val: int) -> Optional[int]:
    """
     Find leftmost value greater than val
    :param lst: given list
    :param val: given value
    :return: found value | None
    """
    i = bisect.bisect_right(lst, val)
    if i != len(lst):
        return lst[i]
    return None


def bysearch_gt(lst: List[int], val: int, is_sorted: bool = True) -> Optional[int]:
    """ binary search algorithm. Find leftmost item greater than 'val'
    :param lst: given list
    :param val: given value
    :param is_sorted: is list sorted
    :return: found value | None
    """

    if not lst:
        return

    if not is_sorted:
        lst.sort()

    len_lst = len(lst)
    left = 0
    right = len_lst - 1

    while left < right:
        center = (left + right) // 2

        if lst[center] <= val:
            left = center + 1 if center <= len_lst - 1 else len_lst - 1
        else:
            right = center

    if lst[right] > val:
        return lst[right]


for _, testcase in enumerate(TESTCASE):
    result = bysearch_gt(lst=testcase[0], val=testcase[1])
    # print(f"result={result}")
    assert result == OUTPUTS[_], f"Testcase #{_ + 1}: output = {OUTPUTS[_]} expected, got: {result}"

    result = find_gt(lst=testcase[0], val=testcase[1])
    # print(f"result={result}")
    assert result == OUTPUTS[_], f"Testcase #{_ + 1}: output = {OUTPUTS[_]} expected, got: {result}"

print("Done.")
