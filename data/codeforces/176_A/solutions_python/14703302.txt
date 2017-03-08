# Shayenne Moura

n, m, l = map(int, raw_input().split())

planet = []

for i in xrange(n):
    nome = raw_input()
    op = []
    for j in xrange(m):
        
        a, b, c = map(int, raw_input().split())

        op.append([a, b, c])

    planet.append(op)


maximo = 0

for i in xrange(n):
    for j in xrange(n):
        if i != j:
            pft = []
            for k in xrange(m):
                luc = planet[j][k][1] - planet[i][k][0]
                pft.append([luc, planet[i][k][2]])
                           
            pft.sort(reverse=True, key=lambda tup:tup[0])

            qtd = 0
            ganho = 0
            for r in xrange(len(pft)):
                if qtd + pft[r][1] <= l and pft[r][0] > 0:
                    ganho += pft[r][0]*pft[r][1]
                    qtd += pft[r][1]
                elif pft[r][0] > 0:
                    ganho += pft[r][0]*(l-qtd)
                    break
            
                          

            if ganho > maximo:
                maximo = ganho

print maximo
