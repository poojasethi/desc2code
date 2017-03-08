I=raw_input
n=I()
m=I()
n=sorted(list(n))
for i in range(len(n)):
    if n[i] != '0':
        break
if n[i] != '0':
    n[0],n[i]=n[i],n[0]
print ['OK', 'WRONG_ANSWER'][n != list(m)]