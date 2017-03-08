n = input()
a = []

h = range(n)


def read_a(i):
    rec = map(lambda _: lambda: read_a(i + 1), h)
    rec[-1] = lambda: 0
    rec[i]()
    a.append(list(map(int, raw_input().split(' '))))
read_a(0)


def iter_i(i):
    rec_i = map(lambda _: lambda: iter_i(i + 1), h)
    rec_i[-1] = lambda: 0

    def iter_j(j):
        rec_j = map(lambda _: lambda: iter_j(j + 1), h)
        rec_j[-1] = lambda: 0

        def iter_k(k):
            rec_k = map(lambda _: lambda: iter_k(k + 1), h)
            rec_k[-1] = lambda: 0
            a[j][k] = min(a[j][k], a[j][i] + a[i][k])
            rec_k[k]()
        iter_k(0)
        rec_j[j]()
    iter_j(0)
    rec_i[i]()
iter_i(0)

print max(map(max, a))
