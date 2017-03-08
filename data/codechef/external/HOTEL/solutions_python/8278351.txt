t = input()
for i in range(0,t):
    n = input()
    l1 = raw_input()
    l1 = l1.split()
    for j in range(0,n):
        l1[j] = int(l1[j])
    l2 = raw_input()
    l2 = l2.split()
    for j in range(0,n):
        l2[j] = int(l2[j])
    l = [0]*1001
    for j in range(0,n):
        for k in range(l1[j],l2[j]):
            l[k]+=1
    print max(l)