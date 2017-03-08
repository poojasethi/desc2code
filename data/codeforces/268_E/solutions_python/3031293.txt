n=input()
v=[0]*n
e,f=0,0
for i in range(n):
  a,b=map(int,raw_input().split())
  e+=a
  v[i]=(a*b,100-b)
v.sort(cmp=lambda x,y:x[1]*y[0]-x[0]*y[1])
for x in v:
  e+=f*x[1]/100.
  f+=x[0]/100.
print '%.12f'%e
