n = int(raw_input())

song = []
for _ in range(n):
    l, p = map(int, raw_input().split())
    song.append([l, p])

def mycmp(a, b):
    return b[0]*b[1]*(100-a[1]) - a[0]*a[1]*(100-b[1])
    
song.sort(mycmp)
ans = 0
love_exp = 0
for l, p in song:
    ans += l
    ans += love_exp * (100.0 - p)/100.0
    love_exp += l * p / 100.0
print ans



    
