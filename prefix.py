def prefix(arr):
    if arr == None or len(arr) == 0:
        return None

    min = len(arr[0])
    minword = arr[0]

    for word in arr[1:]:
        if len(word) < min:
            min = len(word)
            minword = word

    comp = minword

    for i in range(min):
        for word in arr:
            if word[i] != comp[i]:
                return comp[:i]

    return minword


arr = ['flower', 'flora', 'floack', 'flow']
print(prefix(arr))

arr = ['flower']
print(prefix(arr))

arr = ['ab', 'a']
print((prefix(arr)))
