n, k = map(int, raw_input().split())
y = map(int, raw_input().split())
f = filter(lambda x: x < 5 and x+k <= 5, y)
print len(f)/3
