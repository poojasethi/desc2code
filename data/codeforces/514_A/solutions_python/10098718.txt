x = raw_input()
ans = ""
for i in range(len(x)):
    y = 9-int(x[i])
    if i == 0 and y == 0:
        ans += x[i]
    else:
        ans += min(x[i], str(y))
print ans
