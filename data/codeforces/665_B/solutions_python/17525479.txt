l1 = map(int, raw_input().split(' '))
n = l1[0]
m = l1[1]
k = l1[2]

stuff = map(int, raw_input().split(' '))
    

users = []
for x in range(0, n):
    l3 = map(int, raw_input().split(' '))
    users.append(l3)
total = 0
for x in range(0, n):
    for y in users[x]:
        pos = stuff.index(y) + 1
        stuff.remove(y)
        stuff = [y] + stuff
        total = total + pos
print total
