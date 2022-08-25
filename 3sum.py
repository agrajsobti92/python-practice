nums = [0, 0, 0, 0]
nums.sort()

soln = []

for left in range(len(nums) - 2):
    if left > 0 and nums[left] == nums[left - 1]:  # 1
        continue

    mid = left + 1
    right = len(nums) - 1

    # 2
    while mid < right:
        if mid - left > 1 and nums[mid] == nums[mid - 1]:
            mid += 1
            continue
        if len(nums) - right > 1 and nums[right] == nums[right + 1]:
            right -= 1
            continue
        if nums[left] + nums[mid] + nums[right] < 0:
            mid += 1
        elif nums[left] + nums[mid] + nums[right] > 0:
            right -= 1
        else:
            soln.append([nums[left], nums[mid], nums[right]])
            mid += 1  # 2

print(soln)

# 1 Doing this to prevent the same number from being on the leftmost blank i.e
# avoiding duplicates

# 2 Here onwards it's basicalle 2sum II

# 2 Want this loop to continue even after a match is found since for a particular
# left there can be mutliple nums[mid], nums[right] combos
