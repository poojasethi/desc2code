def croc():
    t = input()
    a = map(int,raw_input().split())
    m = min(a)
    flag = 0
    for i in range(t):
        if a[i]%m != 0:
            flag = 1
            break
    if flag == 0:
        print m
    else:
        print -1
croc()
