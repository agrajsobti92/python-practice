nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def binsearch(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = int((left + right) / 2)

        if target > nums[mid]:
            left = mid + 1

        elif target < nums[mid]:
            right = mid - 1

        else:
            return mid

    return False


print(binsearch(nums, 9))
