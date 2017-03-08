import math
s = raw_input()
res = False
ab_loc = s.find("AB")
if s[ab_loc + 2:].find("BA") != -1:
    res = True

ba_loc = s.find("BA")
if s[ba_loc + 2:].find("AB") != -1:
    res = True

if res and ab_loc != -1 and ba_loc != -1:
    print "YES"
else:
    print "NO"