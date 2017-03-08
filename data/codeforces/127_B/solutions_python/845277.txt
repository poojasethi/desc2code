n = input()
l = [int(x) for x in raw_input().split()]

newl = []
pairs = 0
for i in l:
    if i in newl:
        pairs +=1
        newl.remove(i)
    else:
        newl.append(i)

print pairs/2
