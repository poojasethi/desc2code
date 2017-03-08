from itertools import groupby,chain

n = input()
x = map(int, raw_input().split())

print max( [ len(list(g)) for k,g in chain(
    groupby(x, lambda a: a + a%2),
    groupby(x, lambda a: a + 1-a%2)
    ) ] )
