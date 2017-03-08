a = map(int, raw_input().split(" "))
b = map(int, raw_input().split(" "))
n = input()

count = (sum(a)+5-1)//5 + (sum(b)+10-1)//10
if count <= n:
    print "YES"
else:
    print "NO"