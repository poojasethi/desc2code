n = int(raw_input())
for i in range(1, n, 2):
    print (n-i)/2 * '*' + i*'D' + (n-i)/2*'*'
print 'D'*n
for i in range(n-2, 0, -2):
    print (n-i)/2 * '*' + i*'D' + (n-i)/2*'*'


