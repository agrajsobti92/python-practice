nums = [1, 1, 1, 2, 2, 3, 3, 2, 1, 2, 3, 2, 4, 4, 4, 4, 0, 0, 0, -1, -1, -1]
k = 3

d = {}
res = []

for i in range(len(nums) + 2):
    res.append([])

print(res)

for i in nums:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

print(d)

for key, freq in d.items():
    res[freq].append(key)

print(res)

ans = []

for i in range(len(res) - 1, 0, -1):
    for n in res[i]:
        ans.append(n)
        if len(ans) == k:
            print(ans)
