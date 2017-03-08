par = map(int, raw_input().split(" "))
a, b, x, y = par[0], par[1], par[2], par[3]
l, r = 1, 10**10
while r - l > 1:
    m = (l+r) //2
    if (m-m//x < a) or min(m - a - m//(x*y), m - m//y) < b:
        l = m
    else:
        r = m
print r
    
        
