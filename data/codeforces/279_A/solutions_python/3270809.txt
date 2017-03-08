[x, y] = [float(z) for z in raw_input().split()]

if x == 0:
    if y > 0:
        print int(y * 4 - 2)
    else:
        print int(-y * 4)
    exit()

if x == -y + 1:
    print int((x - 1) * 4)
    exit()

z = y/x
if y > 0 and (z <= -1 or z > 1):
    print int(y * 4 - 2)
elif x < 0 and -1 < z <= 1:
    print int(-x * 4 - 1)
elif y < 0 and (z > 1 or z < y/(x + 1)):
    print int(-y * 4)
else:
    print int(x * 4 - 3)


