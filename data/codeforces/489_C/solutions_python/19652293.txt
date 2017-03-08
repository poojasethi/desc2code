# N = input()
N, S = map(int, raw_input().split(" "))

if N*9 < S:
    print -1, -1
elif S == 0:
    if N == 1:
        print 0, 0
    else:
        print -1, -1
else:
    if N > 1:
        nines = S / 9
        r = S % 9
        zeros = N - nines - 1
        if N - nines == 0:
            M = "9"*nines
        else:
            M = "9"*nines+str(r)+"0"*zeros
        nines = (S-1) / 9
        r = (S-1) % 9
        if N - nines == 1:
            m = str(r + 1) + "9"*nines
        else:
            m = "1" + "0"*(N - nines - 2) + str(r) + "9"*nines
        print m, M
    else:
        print S, S
