s1 = "adc"
s2 = "dcda"

d1 = {}
d2 = {}

for ch in s1:
    d1[ch] = 1 + d1.get(ch, 0)

print(d1)

left = 0

for right in range(len(s2)):
    d2[s2[right]] = 1 + d2.get(s2[right], 0)
    print(d2)
    win_size = right - left + 1
    if win_size == len(s1):
        if d1 == d2:
            print(True)
            break
        if d2[s2[left]] > 1:
            d2[s2[left]] -= 1
        else:
            d2.pop(s2[left])
        left += 1


print(False)
