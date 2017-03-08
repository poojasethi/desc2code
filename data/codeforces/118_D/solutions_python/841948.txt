# coding: utf-8
N1, N2, k1, k2 = map(int, raw_input().split())
mod = 100000000
memo = dict()

def dfs(n1, n2, seq, turn):
    global k1, k2

    if n1 < 0 or n2 < 0 :
        return 0

    #print "n1=%d , n2=%d , seq=%d , turn=%d" % (n1, n2, seq, turn)

    if n1 == 0 and n2 == 0:
        return 1

    if memo.has_key((n1, n2, seq, turn)):
        return memo[(n1, n2, seq, turn)]

    res = 0
    if turn == 0 :
        res += dfs(n1, n2-1, 1, 1)
        res %= mod
        if seq < k1 :
            res += dfs(n1-1, n2, seq+1, turn)
            res %= mod
        
    else:
        res += dfs(n1-1, n2, 1, 0)
        res %= mod
        if seq < k2 :
            res += dfs(n1, n2-1, seq+1, turn)
            res %= mod

    memo[(n1, n2, seq, turn)] = res
    return res



print (dfs(N1-1, N2, 1, 0) + dfs(N1, N2-1, 1, 1)) % mod
