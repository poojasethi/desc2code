s = raw_input()
a4=a7=0

for i in s:
    if i=="4":
        a4+=1
    elif i=="7":
        a7+=1

if a4==0 and a7==0:
    print -1
elif a4>=a7:
    print 4
else:
    print 7
