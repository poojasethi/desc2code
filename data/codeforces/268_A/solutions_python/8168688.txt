s = [raw_input().split() for i in range(input())]


print sum(x[0]==y[1] for x in s for y in s)
