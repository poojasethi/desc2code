import sys

n = int(raw_input())
s = raw_input()

mas = map(int,s.split())
ans = list()

sum1=0
sum2=0

for i in range(n-1,-1,-1):
    if sum1<=sum2:
        sum1=sum1+mas[i]
        ans.append(0) # '+'
    else:
        sum2=sum2+mas[i]
        ans.append(1) # '-'
ans.reverse()
for i in range(n):
    if sum1<sum2:
        ans[i]=1-ans[i]
    if ans[i]==0:
        sys.stdout.write('+')
    else:
        sys.stdout.write('-')
