import math

def ncr(n,r):
    f=math.factorial
    return  f(n)/f(r)/f(n-r)


ori = raw_input()
rep = raw_input()

orifo = ori.count('+')
orire = ori.count('-')

repfo = rep.count('+')
repre = rep.count('-')
repun = rep.count('?')

if orifo == repfo and repun==0:
    pro = 1
elif repun==0 and repfo!=orifo:
    pro = 0
elif repfo > orifo or repre>orire:
    pro = 0
else:
    re = orire-repre
    fo = orifo-repfo
    pro = ncr(repun, re)*((0.5)**repun)

print pro
    
