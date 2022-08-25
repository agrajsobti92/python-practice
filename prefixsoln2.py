def prefix(strs):
    if not strs:
        return ""
    shortest = min(strs, key=len)
    for i, ch in enumerate(shortest):
        for other in strs:
            if other[i] != ch:
                return shortest[:i]
    return shortest


arr = ['flower', 'flora', 'floack', 'flow']
min(arr, key=)
print(prefix(arr))

arr = ['flower']
print(prefix(arr))

arr = ['ab', 'a']
print((prefix(arr)))
