n, m = map(int, raw_input().split())
xs = sorted(map(int, raw_input().split()))

print -sum(filter(lambda x: x < 0, xs)[:m])
