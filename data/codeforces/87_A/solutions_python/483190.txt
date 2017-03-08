a, b = map(int, raw_input().split())

suma, sumb = 0, 0
na, nb, t = a, b, 0

while na != nb:
    if na < nb:
        suma += na-t
        t += na-t
        na += a
    elif nb < na:
        sumb += nb-t
        t += nb-t
        nb += b

if a > b:
    suma += na-t
else:
    sumb += nb-t

if suma > sumb:
    print "Dasha"
elif sumb > suma:
    print "Masha"
else:
    print "Equal"
