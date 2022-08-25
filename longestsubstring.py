s = "abcabcbbefghijklmnopzaaaaa"
# s= 'bbbb'

charset = set()
left = 0
max = 0

for right in range(len(s)):

    if s[right] in charset:
        while s[right] in charset:
            charset.remove(s[left])
            left += 1

    charset.add(s[right])

    print(charset)

    if len(charset) > max:
        max = len(charset)

print(max)
