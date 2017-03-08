n,m = map(int, raw_input().split())
names = [raw_input() for i in range(n)]
print(reduce(lambda a,b: a*b, [len(set([j[i] for j in names])) for i in range(m)]) %1000000007)
