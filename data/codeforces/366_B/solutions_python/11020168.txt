_, k = map(int, raw_input().split())
ns = map(int, raw_input().split())

print min([(sum(ns[i::k]), i) for i in range(k)])[1] + 1