fctrl = list()
fctrl.append(1);
var=1;
for x in range(1,101):
	var=var*x
	fctrl.append(var);

t=raw_input()
t=int(t)
for x in range(0,t):
	y=raw_input()
	y=int(y)
	print fctrl[y]