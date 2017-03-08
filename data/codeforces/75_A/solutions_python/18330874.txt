n1 = input()
n2 = input()
print "YES" if (int(str(n1).replace('0','')) + int(str(n2).replace('0','')) == int(str(n1+n2).replace('0',''))) else  "NO"
