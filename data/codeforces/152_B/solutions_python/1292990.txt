n, m = map(int,raw_input().split())
x, y = map(int,raw_input().split())
k = int(input())
s = 0;

def ms(x,dx,n):
    return (n-x)//dx if dx>0 else -(x-1)//dx if dx else 100000000001

for i in range(k):
    dx, dy = map(int,raw_input().split())
    r = min(ms(x,dx,n),ms(y,dy,m))
    x+=dx*r; y+=dy*r; s+=r
    
print(s)
