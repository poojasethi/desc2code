n=int(raw_input())
b=[int((n>>i)& 1) for i in range(32)]
print sum(b)