from typing import List


def containsDuplicate(nums: List[int]) -> bool:
    hashset = set()

    for n in nums:
        if n in hashset:
            return True
        hashset.add(n)
    return False


def alternatesoln(nums):
    l = len(nums)
    for i in range(l - 1):
        for j in range(i + 1, l):
            if nums[i] == nums[j]:
                return True
    return False


list = [1, 2, 3, 1]
print(containsDuplicate(list))
print(alternatesoln(list))
