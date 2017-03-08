n = input()
t = n*(n-1)/2*(n-2)/3*(n-3)/4*(n-4)/5
res = t
t = t*(n-5)/6
res = res + t
t = t*(n-6)/7
res = res + t
print res