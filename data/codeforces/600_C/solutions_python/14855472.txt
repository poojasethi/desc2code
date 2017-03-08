from collections import OrderedDict

s = raw_input()
d = dict()

for i in s:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

odd = dict()
for i in d:
    if (d[i] % 2 != 0):
        odd[i] = d[i]


odd = OrderedDict(sorted(odd.items()))

while True:
    if (len(odd) <= 1):
        break
    
    i = odd.keys()[0]
    j = odd.keys()[-1]
   
    odd.pop(i)
    odd.pop(j)
    
    d[i] += 1
    d[j] -= 1

s = ""

d = OrderedDict(sorted(d.items()))

for i in d:
    cnt = d[i]/2
    while cnt > 0:
        s += i
        cnt -= 1

c = ''
if (len(odd) == 1):
    c = odd.keys()[0]
print s + c + s[::-1]
