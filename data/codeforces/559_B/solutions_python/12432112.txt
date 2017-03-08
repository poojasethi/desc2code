def check(a,b):
    #print "checking %s : %s" %(a,b)
    l = len(a)
    if(l%2==1):
        return a==b
    if(a==b):
        return True
    l = l/2
    #print "l = "+str(l)
    return (check(a[:l],b[l:]) and check(a[l:],b[:l])) or (check(a[:l],b[:l]) and check(a[l:],b[l:]))

a = raw_input()
b = raw_input()
if(check(a, b)):
    print "YES"
else:
    print "NO"
