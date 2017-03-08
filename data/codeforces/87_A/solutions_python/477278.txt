def gcd(a,b):
    return a if (b==0) else gcd(b,a%b)
a,b=map(int,raw_input().split())
g=a*b/gcd(a,b)
if (g/min(a,b)==g/max(a,b)+1):print("Equal")
elif (a<b):print("Dasha")
else: print("Masha")