s = "ABAB"
k = 2

left = 0
char = {}
res = 0


for right in range(len(s)):
    if s[right] not in char:
        char[s[right]] = 1
    else:
        char[s[right]] += 1

    win_len = right - left + 1

    maxf = 0

    for i in char:
        if char[i] > maxf:
            maxf = char[i]

    if win_len - maxf <= k:
        res = win_len
    else:
        char[s[left]] -= 1
        left += 1


print(res)
