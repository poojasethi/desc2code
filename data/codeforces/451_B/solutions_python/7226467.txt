n = int(raw_input())
a = map(int, raw_input().split())

pb = n
for i in range(0,n-1):
    if a[i] > a[i+1]:
        pb = i
        break

if pb == n:
    print 'yes\n1 1'
else :
    pe = n
    for i in range(pb,n-1):
        if a[i] < a[i+1]:
            pe = i + 1
            break
    if a[0:pb]+a[pb:pe][::-1]+a[pe:] == sorted(a):
        print 'yes\n'+str(pb+1)+' '+str(pe)
    else:
        print 'no'
