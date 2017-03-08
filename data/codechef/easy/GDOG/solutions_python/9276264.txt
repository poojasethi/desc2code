T = int(raw_input())

for i in range(T):
    N, K = map(int, raw_input().split())
    r_max = 0
    found = False
    while(K > 0 and not found):
        if N % K >= r_max:
            r_max = N % K
        else:
            found = True
        K -= 1
    print r_max
    

                
