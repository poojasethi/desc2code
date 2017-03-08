n, m = raw_input().split(' ')
n = (int)(n)
m = (int)(m)
x = n/m
y = n % m
for i in range(m-y):
    print x,
    
for i in range(y):
    print x + 1,
