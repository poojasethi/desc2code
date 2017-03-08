b=int(raw_input())
a=raw_input()

j=0

for i in range(b-1):
    if a[i]==a[i+1]:
        j+=1
print j
