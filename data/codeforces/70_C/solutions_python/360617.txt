from collections import defaultdict
from fractions import gcd

(max_x, max_y, w) = map( int, raw_input().split() )

def Pair(x):
    inv_x = 0
    val = x
    while val:
        inv_x = inv_x * 10 + val % 10
        val /= 10
    uc = gcd( x, inv_x )
    return ( x/uc, inv_x/uc )

def Reverse(P):
    return ( P[1], P[0] )

MapX = defaultdict(int)
MapY = defaultdict(int)
for y in xrange(1, max_y+1):
    MapY[ Pair(y) ] += 1
    
y = max_y
lucky_tickets = 0
res = ( 100007, 100007 )
for x in xrange(1, max_x+1):
    lucky_tickets += MapY[ Reverse( Pair(x) ) ]
    MapX[ Pair(x) ] += 1
    while (y > 0)and( lucky_tickets - MapX[ Reverse( Pair(y) ) ] >= w ):
        lucky_tickets -= MapX[ Reverse( Pair(y) ) ]
        MapY[ Pair(y) ] -= 1
        y -= 1
        
    if (lucky_tickets >= w) and ( x * y < res[0] * res[1] ):
        res = (x, y)
        
if res[0] == 100007:
    print -1
else:
    print "%d %d" % res