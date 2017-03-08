n = input()
a = 1
b = n*n
for i in xrange(n):
    for j in xrange(n/2):
        print a,b,
        a+=1
        b-=1
    print ""
