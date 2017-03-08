# coding =utf-8
n,o=0,sorted([map(int,raw_input().split()) for _ in range(int(input()))])
for a,b in o: n=a if b<n else b
print n