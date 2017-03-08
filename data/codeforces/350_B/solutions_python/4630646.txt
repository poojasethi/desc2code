import sys

inputs = sys.stdin.readline().split()
n = int(inputs[0])
l = [0] * n

sites = sys.stdin.readline().split()
hotels = set()
for i in xrange(n):
    if sites[i] == '1':
        hotels.add(i)

tracks = sys.stdin.readline().split()
tracks = [int(j) for j in tracks]
s = set()
d = {}

for i in xrange(n):
    start = tracks[i] - 1
    if (start in s):
        l[i] = -1
        l[d[start]] = -1
    else:
        l[i] = start
    s.add(start)
    d[start] = i

def go_back(hotel):
    tmp = 1
    i = hotel
    while (l[i] != -1):
        tmp += 1
        i = l[i]
    return tmp

#print l
max_length = 0
max_hotel = 0
for hotel in hotels:
    t = go_back(hotel)
    if (t >= max_length):
        max_length = t
        max_hotel = hotel

#print max_hotel
#print max_length
result = []
result.append(max_hotel + 1)
i = max_hotel
while (l[i] != -1):
    result.append(l[i] + 1)
    i = l[i]


l = len(result)
print l
for i in xrange(l-1, -1, -1):
    print result[i],
