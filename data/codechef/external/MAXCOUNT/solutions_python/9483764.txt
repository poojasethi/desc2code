t = int(raw_input())

for i in range(t):
    n = int(raw_input())
    a = raw_input().split(' ')
    a = map(int, a)
    counts = []
    for j in range(n):
        counts.append(a.count(a[j]))

    max_count = max(counts)
    max_count_indices = []
    for j in range(n):
        if max_count == counts[j]:
            max_count_indices.append(j)

    x = [a[l] for l in max_count_indices]
    print min(x), max_count
