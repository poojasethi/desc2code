def don(a,b):
    if a==0 :
        return '0'
    ret=''
    while a :
        ret+=d[a%b]
        a/=b
    return ret[::-1]
def dor(a,s,r):
    if not s:
        return ''
    else :
        if a >=s[0]:
            return r[0]+dor(a-s[0],s,r)
        else :
            return dor(a,s[1:],r[1:])
s=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
r=["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
d="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
a,b=raw_input().split()
c=raw_input().strip()
a=int(c,int(a))
if b=='R' :
    print dor(a,s,r)
else :
    print don(a,int(b))
