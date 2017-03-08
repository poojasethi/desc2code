n,m,x,y,a,b = map(int,raw_input().split())
v = 1<<60
for c in [(1,m),(n,1),(n,m),(1,1)]:
  dx=abs(x - c[0])
  dy=abs(y - c[1])
  if 0==dx+dy:
    v=0
  elif dx%a==0 and dy%b==0 and (dx/a)%2==(dy/b)%2:
    v=min(v,max(dx/a,dy/b))
if v and (max(n-x,x-1)<a or max(m-y,y-1)<b):
  v=1<<60
print ("Poor Inna and pony!",v)[v<(1<<55)]