x = int(raw_input())
b = bin(x)
print sum([1 if d == '1' else 0 for d in b])
