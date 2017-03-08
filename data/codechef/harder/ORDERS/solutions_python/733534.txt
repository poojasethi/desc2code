import sys
 
def newInsert(l, insertPos, x):
    maxLength = 400
    pos = 0
    listpos = 0
    while len(l[listpos]) < insertPos:
        insertPos -= len(l[listpos])
        listpos +=1
 
    # now need to insert value x at position insertPos in list #listpos
 
    l[listpos].insert(insertPos, x)
 
    # check if maxLength exceeded
 
    if len(l[listpos]) >= maxLength:
        l.insert(listpos+1, l[listpos][maxLength//2:])
        l[listpos] = l[listpos][:maxLength//2]       

# wrong algorithm below!
 
def main():
    nCases = int(sys.stdin.readline())
     
    for case in range(nCases):
        nSoldier = int(sys.stdin.readline())
        moves = map(int, sys.stdin.readline().split())
     
        order = [[]]
        for pos in range(nSoldier):
            move = moves[pos]
            newInsert(order, pos-move, pos+1)
            #newOrder = order[:(pos-move)] + [pos+1] + order[(pos-move):]
            #order = newOrder

        reorder = [0] * nSoldier

        pos = 1
        for sublist in order:
            for rank in sublist:
                reorder[rank-1] = pos
                pos +=1
                
        for rank in reorder:
            print rank,
        print
 
if __name__ == '__main__' :
    try:
        import psyco
        psyco.full()
    except ImportError:
            pass     
    main()    
 