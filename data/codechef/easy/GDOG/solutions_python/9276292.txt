T = int(raw_input())

for i in range(T):
    N, K = map(int, raw_input().split())
    r_max = 0
    while(K > 0):
        if N % K >= r_max:
            r_max = N % K
        else:
            break
        K -= 1
    print r_max
    

                
