T = int(raw_input())

for it in range(T):
    N, K = map(int, raw_input().split())
    foreign  = raw_input().split()
    mapping  = [0 for i in range(N)]
    for i in range(K):
        modern = raw_input().split()
        for j in range(N):
            if foreign[j] in modern:
                mapping[j] = 1
    print ' '.join(map(lambda x: "YES" if x else "NO", mapping))
