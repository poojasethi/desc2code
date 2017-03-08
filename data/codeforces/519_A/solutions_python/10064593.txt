pt = {"Q":9, "q":9, "R":5, "r":5, "B":3, "b":3,
        "N":3, "n":3, "P":1, "p":1, "K":0, "k":0}
w = b = 0
for loop in xrange(8):
    line = raw_input()
    for i in line:
        if i == ".": continue
        if i.isupper(): w += pt[i]
        else:           b += pt[i]
if   w > b: print "White"
elif b > w: print "Black"
else:       print "Draw"
