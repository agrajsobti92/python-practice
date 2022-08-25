piles = [312884470]


def minEatingspeed(piles, h):

    l, r = 1, max(piles)
    k = 0

    while l <= r:
        m = (l + r) // 2
        hours = 0
        for num in piles:
            hours += ((num - 1) // m) + 1
        if hours <= h:
            k = m
            r = k - 1
        elif hours > h:
            l = k + 1
    return k


print(minEatingspeed(piles, 312884469))
