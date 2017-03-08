
n = int(raw_input())

s1 = list(raw_input())
s2 = list(raw_input())

maior = menor = 0
antes = depois = igual = 1
poss = 1

for i in xrange(n):

    if s1[i] != "?":
        if s2[i] != "?":
            if int(s1[i]) > int(s2[i]):
                maior += 1
                antes = 0 
                igual = 0
            elif int(s1[i]) < int(s2[i]):
                menor += 1
                depois = 0
                igual = 0
           
        else:
            antes *= 10 - int(s1[i])
            depois *= int(s1[i]) + 1
            poss *= 10
    else:
        if s2[i] != "?":
            antes *= int(s2[i]) + 1
            depois *= 10 - int(s2[i])
            poss *= 10
        else:
            antes *= 55
            depois *= 55
            igual *= 10
            poss *= 100

    antes = antes % 1000000007
    depois = depois % 1000000007
    igual = igual % 1000000007
    poss = poss % 1000000007
    

if maior != 0 and menor != 0:
    print (poss) % 1000000007
    exit(0)
            
print (poss - antes - depois + igual) % 1000000007
