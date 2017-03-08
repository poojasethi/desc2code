
n = int(raw_input())
a = int(n/36)
b = int(n%36/3)+(1 if n%3>1 else 0)

if b >= 12:
    a += 1
    b -= 12

print a, b
