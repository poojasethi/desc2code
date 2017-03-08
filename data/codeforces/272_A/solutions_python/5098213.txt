n = input()

s = sum(map(int,raw_input().split()))

k = n+1
temp=0
for i in range(5):
    if (s+i)%k==0:
        temp += 1

print(5-temp)