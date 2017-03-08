s = raw_input();
t = raw_input();
sh, sm = map(int, s.split(':'));
th, tm = map(int, t.split(':'));
if (s < t):
	sh += 24;
if sm < tm:
	sm += 60;
	sh -=1;
print ("%02d:%02d") % (sh-th, sm-tm)

