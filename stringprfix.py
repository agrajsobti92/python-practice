def main():
    strs = ["flower", "flow", "flight", "fight"]
    print(palindrome(strs))


def palindrome(strs):
    if not strs:
        return ""

    shortest = min(strs, key=len)

    for i, ch in enumerate(shortest):
        for other in strs:
            if other[i] != ch:
                return shortest[:i]
    return shortest


main()
