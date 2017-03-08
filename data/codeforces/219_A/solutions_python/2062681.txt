n=int(raw_input())
s=raw_input()
d={}
for c in s:
    d[c]=d.get(c,0)+1
for a,b in d.items():
    if b%n!=0:
        print -1
        raise SystemExit()
print ("".join([a*(b/n) for a,b in d.items()]))*n
