n = int(raw_input())

a = n/2
b = 1

for i in range(n):
    print "*" * a + "D" * b + "*" *a
    if i < n/2:
        a -= 1
        b += 2
    else:
        a += 1
        b -= 2
