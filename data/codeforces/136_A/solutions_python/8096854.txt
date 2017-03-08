T = input()

s = map(int,raw_input().split())

for i in range(len(s)):
    print s.index(i+1)+1,
    
