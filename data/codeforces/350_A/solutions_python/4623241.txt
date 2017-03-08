[n, m] = map (int, raw_input().split());

a = map (int, raw_input().split());
b = map (int, raw_input().split());

tl = max (2 * min(a), max(a));

if tl < min(b):
	print tl
else:
	print "-1"
