def modPow(base, pow, mod):
    ret = 1
    while pow > 0:
        if (pow % 2) == 0:
            base = (base * base) % mod
            pow >>= 1
        else:
            ret = (ret * base) % mod
            pow = pow - 1
    return ret;

a, b, n, x = map(int, raw_input().split())
modulo = 1000000007

first = modPow(a,n,modulo)
second = x % modulo
third = 0
if a != 1:
    third = modPow(a, n, modulo * (a - 1))
    third = modulo * (a - 1) - 1 if third == 0 else third - 1
    third = third / (a - 1) * b
else:
    third = (b * n) % modulo
ans = (((first * second) % modulo) + third % modulo) % modulo
print ans