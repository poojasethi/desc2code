par = map(int, raw_input().split(" "))
k, n, m, q = par[0], par[1], par[2], par[3]

basic = {}
basic2 = {}
index = 0
for i in range(n):
    temp = raw_input()
    basic[temp] = index
    basic2[index] = temp
    index += 1
    

composite = {}
for i in range(m):
    par = raw_input().split(": ")
    art = par[0]
    names = par[1].split(", ")
    
    temp = {}
    for item in names:
        b = item.split(" ")
        temp[basic[b[0]]] = int(b[1])
    
    composite[art] = temp

purchase = [[0 for i in range(len(basic))] for i in range(k)]
for i in range(q):
    par = raw_input().split(" ")  
    purchase[int(par[0])-1][basic[par[1]]] += 1

'''
print "\n"
print basic
print basic2
print composite
print purchase
print "\n"
'''

for player in purchase:
    #print player

    gen = []
    
    cangen = []
    for item in composite:
        count = 101
        genArt = True
        for b in composite[item]:
            #print b, player[b], composite[item][b]
            if player[b] < composite[item][b]:
                genArt = False
                break
            else:
                count = min(count, player[b]/composite[item][b])
                
        if genArt == True:
            cangen.append([count, item])
    

    if len(cangen) > 0:
        cangen.sort(reverse = True)
        gen.append([cangen[0][1], cangen[0][0]])
        for b in composite[cangen[0][1]]:
            player[b] -= composite[cangen[0][1]][b] * cangen[0][0]
    
    #print cangen, gen, player
    
    for i in range(len(player)):
        if player[i] != 0:
            gen.append([basic2[i], player[i]])

    
    print len(gen)
    gen.sort()
    for item in gen:
        print item[0] + " " + str(item[1])

    