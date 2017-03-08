def check(b,g):
    if g==b: return True
    if b>g: return b<=2*g+2
    else: return abs(g-b)<=1
gl,gr=map(int,raw_input().split())
bl,br=map(int,raw_input().split())
if check(bl,gr) or check(br,gl): print "YES"
else: print "NO"
