n = input()
choco = map(int, raw_input().split())
s = sum(choco)
alice = 0
t = 0
for c in choco:
    alice += 1
    t += c * 2
    if t == s:
        break
    elif t > s:
        if (t - s) > (s - (t - c * 2)):
            alice -= 1
        break

print alice, n - alice
