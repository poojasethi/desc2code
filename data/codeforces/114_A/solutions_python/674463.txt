k = input()
l = input()

count = 0
m = k
while m<l:
    m *= k
    count += 1

if m==l:
    print "YES"
    print count
else:
    print "NO"

   
