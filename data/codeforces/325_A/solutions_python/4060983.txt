n = int(raw_input())

lx=1000000000
ly=1000000000
rx=0
ry=0
area=0
for i in range(0,n):
  a,b,c,d=map(int,raw_input().split())
  if a<lx :
    lx=a
  if c > rx:
    rx=c
  if b < ly:
    ly=b
  if d > ry:
    ry=d
  area+=(c-a)*(d-b)

if area==(rx-lx)*(ry-ly) and rx-lx == ry-ly :
  print "YES"
else:
  print "NO"
