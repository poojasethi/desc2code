a,b = map(int,raw_input().split(':'))
c,d = map(int,raw_input().split(':'))
e,f = a-c,b-d
if f<0: 
        f += 60
        e -= 1
if e<0: e += 24
print '%02d:%02d' % (e,f)
