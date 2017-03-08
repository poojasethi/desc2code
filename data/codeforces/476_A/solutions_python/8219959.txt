n,m = map( int, raw_input().split() )
ans = n / 2 + n % 2
ans += -ans % m
print -1 if ans > n else ans
