#int(raw_input())
#[ int(_) for _ in raw_input().split() ]

n, k, l, r, Sall, Sk = [ int(_) for _ in raw_input().split() ]


if k:
  a = Sk / k
  r = Sk % k
  
  for i in xrange(r):
      print a + 1,
  
  for i in xrange( k - r ):
    print a ,


Sk = Sall - Sk

if n - k:
  a = Sk / (n - k)
  r = Sk % (n - k)
  
  for i in xrange(r):
      print a + 1,
  
  for i in xrange( n - k - r ):
    print a ,
