s = raw_input();
len_s = len(s)
heavy_amount, all = 0, 0;
for i in xrange(len_s-4):
	if s[i:i+5] == "heavy":
		heavy_amount += 1;
	elif s[i:i+5] == "metal":
		all += heavy_amount;
print all;
