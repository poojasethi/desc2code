f,ans=[0]*input(),0
for j,v in enumerate(map(int,raw_input().split())):
    f[v-1]=j
for i in xrange(j):
    ans += abs(f[i]-f[i+1])
print ans
