def fun(s):
    new_s = ""
    for ch in s:
        if ch.isalnum():
            new_s += ch.lower()
    print(new_s)
    print(new_s[::-1])
    if new_s[:] == new_s[::-1]:
        return True
    return False


s = 'A man, a plan, a canal: Panama'
print(fun(s))
