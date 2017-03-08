n, nums, v, i, tl = int(raw_input()), map(int, raw_input().split()), set(), 0, True
t = 0
while len(v) < n:
    if i == n and tl:
        i = n-1
        tl = False
        t += 1
    elif i == -1 and not tl:
        i = 0
        tl = True
        t += 1

    if tl:
        if len(v) >= nums[i] and not i in v:
            v.add(i)
        i += 1
    else:
        if len(v) >= nums[i] and not i in v:
            v.add(i)
        i -= 1
print t
