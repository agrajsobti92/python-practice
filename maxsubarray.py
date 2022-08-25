nums = [-2, -3, 4, -1, -2, 1, 5, -3]


def maxSubArray(nums):

    if len(nums) == 0:
        return 0

    max = 0

    for i in range(len(nums) - 1):
        sum = nums[i]
        for j in range(i + 1, len(nums)):
            sum += nums[j]
            if sum > max:
                max = sum

    return max


print(maxSubArray(nums))
