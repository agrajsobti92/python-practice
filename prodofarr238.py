# nums = [-1, 1, 0, -3, 3]
nums = [1,2,3,4]

res = []
for i in range(len(nums)):
    res.append(1)

prefix = 1
for i in range(len(nums)):
    res[i] = prefix
    prefix = prefix * nums[i]

postfix = 1
for i in range(len(nums) - 1, -1, -1):
    res[i] = res[i] * postfix
    postfix = postfix * nums[i]

print(res)
