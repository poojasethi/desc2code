s = raw_input()
s2 = raw_input().split()

m1 = '6789TJQKA'

i = 0
for ts in m1:
    if ts == s2[0][0]:
        r1 = i
    i+=1

i = 0
for ts in m1:
    if ts == s2[1][0]:
        r2 = i
    i+=1

#print r1, r2

if s2[0][1] != s2[1][1] and s2[0][1] == s[0]:
    print ('YES')
elif s2[0][1] == s2[1][1] and r1 > r2:
    print('YES')
else:
    print('NO')
