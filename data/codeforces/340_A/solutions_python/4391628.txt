from fractions import gcd
a,b,c,d = [int(x) for x in raw_input().split()]
lcm = a*b/gcd(a,b)
print (max(c,d)/lcm - (min(c,d)-1)/lcm)

