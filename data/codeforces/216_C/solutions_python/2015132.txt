n,m,k = map(int,raw_input().split())
hire = ['1']*k + [str(n)]
if n - m >= 2:
    hire += [str(n)]*(k-1)
else:
    hire += [str(n+1)] * (k-1)
    if k == 1 and (n - m == 1 or n == 2):
        hire += [str(n+1)]
    if n == m:
        hire += [str(n+2)]

print len(hire)
print ' '.join(hire)


