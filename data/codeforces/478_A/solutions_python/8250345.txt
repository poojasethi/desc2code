c = map(int, raw_input().split())
s = sum(c)
print -1 if s == 0 or s % len(c) != 0 else s/len(c)