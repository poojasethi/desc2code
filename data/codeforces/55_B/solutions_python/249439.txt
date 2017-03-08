import itertools
res = 100000000000000000000000000
a = raw_input().split()
z = raw_input().split()
for c in itertools.permutations(a):
        res = min(res,eval('(('+c[0]+z[0]+c[1]+')'+z[1]+c[2]+')'+z[2]+c[3]))
        res = min(res,eval('('+c[0]+z[0]+c[1]+')'+z[2]+'('+c[2]+z[1]+c[3]+')'))
print(res)