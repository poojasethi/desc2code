n = input()
c = [0]*10
for i in range(4):
    for j in list(raw_input()):
        if (j!='.'):
            c[int(j)]+=1
print ['NO','YES'][max(c)<=n*2]