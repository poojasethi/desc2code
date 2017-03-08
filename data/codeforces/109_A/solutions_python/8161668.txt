n = input()
ans = []
x,y = 0,0
for i in xrange((n/4)+1):
    if (n-4*i) % 7 == 0:
        x = i
        y = (n - 4*x)/7
        break
print ['4' * x + '7' * y,-1][x == 0 and y == 0]