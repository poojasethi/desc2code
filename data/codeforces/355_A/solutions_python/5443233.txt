k, d = map(int, raw_input().split());

print "No solution" if k > 1 and d == 0 else str(d)+'0'*(k-1)
