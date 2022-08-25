strs = ["eat", "tea", "tan", "ate", "nat", "bat", "hate", "thae", "ant"]
Output = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]

d = {}
ans = []

for word in strs:
    sortedword = ''.join(sorted(word))
    if sortedword in d:
        d[sortedword].append(word)
    else:
        d[sortedword] = [word]

for key in d:
    ans.append(d[key])

print(ans)
