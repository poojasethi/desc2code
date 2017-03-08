t = int(raw_input())
for i in range (t):
    x = int(raw_input())
    pies = sorted(map(int, raw_input().split(' ')))
    racks = sorted(map(int, raw_input().split(' ')))

    count = 0
    for k in range(x):
        pie = pies[k]
        for l in range(x):
            if pie <= racks[l]:
                count += 1
                racks[l] = -1
                break
    print count
