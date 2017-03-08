n, t, c = map(int, raw_input().split());
a = map(int, raw_input().split());
beg = 0;
end = -1;
ans = 0;
for i in xrange(n):
	if a[i] > t:
		if end - beg + 1 >= c:
			ans += (end-beg+2-c);
		beg = i+1;
		i += 1;
	else:
		end = i;
ans += (end-beg+2-c if end-beg+1>=c else 0);
print ans
