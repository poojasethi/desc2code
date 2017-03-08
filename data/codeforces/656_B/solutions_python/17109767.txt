from fractions import gcd

n = input()
m = map(int, raw_input().split())
r = map(int, raw_input().split())

count = 0
days = 100000

for i in range(days):
  for j in range(len(m)):
    if i%m[j]==r[j]:
      count+=1
      break
  
print float(count)/days
