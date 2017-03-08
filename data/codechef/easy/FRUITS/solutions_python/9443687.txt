T = int(raw_input())

for it in range(T):
    N, M, K = map(int, raw_input().split())
    diff = abs(N-M)
    if diff < K:
        print 0
    else:
        print diff-K
