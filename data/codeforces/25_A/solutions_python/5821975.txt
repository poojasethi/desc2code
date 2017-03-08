n=input()
l=[int(i)%2 for i in raw_input().split()]
x=1-(sum(l[:3])&2)/2
print l.index(x)+1