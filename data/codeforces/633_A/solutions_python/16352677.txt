s = raw_input()
s1 = s.split(" ")
a = int(s1[0])
b = int(s1[1])
c = int(s1[2]) 
fl = 0 
ran = c/a + 1 
for i in range(ran):
    prod = a*i 
    if ((c-prod) % b == 0):
        print "Yes"
        fl = 1
        break
if (fl == 0):
    print "No"
        