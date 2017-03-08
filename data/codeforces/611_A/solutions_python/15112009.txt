j,_,w = raw_input().split()
if w == "week":
    ans = 52
    if j in '56': ans += 1
else:
    ans = {'31':7, '30':11}.get(j, 12)
print ans
