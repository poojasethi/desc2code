T = int(raw_input())

for it in range(T):
    N = int(raw_input())
    a = map(int, raw_input().split())
    nDecArrays = []
    start = 0
    end = 1
    while(end != N):
        if a[end] < a[end-1]:
            nDecArrays.append(end-start)
            start = end
        end += 1
    nDecArrays.append(end-start)
    f = sum_of_n_natural_nums = lambda n : n*(n+1)/2
    print sum(map(f, nDecArrays))
