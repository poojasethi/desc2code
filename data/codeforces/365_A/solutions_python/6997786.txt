n, k = map( int, raw_input().split() )
ans = 0
k+=1
for i in xrange( n ):
    if "".join( sorted( list( set( raw_input() )  ) ))[:k] == "0123456789"[:k]:
            ans += 1
print ans
