import math, itertools, sys
x1, y1, x2, y2, x3, y3 = map(int, raw_input().split())

r1, r2, r3 = (x1, y1, 'A'), (x2, y2, 'B'), (x3, y3, 'C')
rects = [r1, r2, r3]
rects.sort()
result = True
sum_areas = 0
for r in rects:
    a = r[0]*r[1]
    sum_areas += a

def can_place(r, board, i, n, orien):
    if orien == 1:
        r = (r[1], r[0], r[2])
    left = 0
    right = r[0] - 1
    up = i
    down = i + r[1] - 1
    #print "Can place"
    #print r
    while right < n and down < n:
        if board[up][left] == 0 and board[up][right] == 0 and board[down][left] == 0 and board[down][right] == 0:
            #print "True at:" + str((left, right, up, down))
            return (True, left)
        left += 1
        right += 1
    return (False, None)

def place(r, board, row, col, n, orien):
    if orien == 1:
        r = (r[1], r[0], r[2])
    #print r, row, col
    for i in xrange(row, row+r[1]):
        for j in xrange(col, col+r[0]):
            board[i][j] = r[2]
    #print board

def all_placed(board, n):
    for i in xrange(n):
        for j in xrange(n):
            if board[i][j] == 0:
                return False
    return True

def print_board(board, n):
    for i in xrange(n):
        line = ''.join(board[i]).strip()
        print line

if int(math.sqrt(sum_areas)) != math.sqrt(sum_areas):
    result = False
    print -1
    sys.exit()

if result == True:
    n = int(math.sqrt(sum_areas))
    for order in itertools.permutations(rects):
        board = [[0 for i in xrange(n)] for j in xrange(n)]
        for r in order:
            for i in xrange(n):
                d = can_place(r, board, i, n, 0)
                if d[0]:
                    place(r, board, i, d[1], n, 0)
                    break
                d = can_place(r, board, i, n, 1)
                if d[0]:
                    place(r, board, i, d[1], n, 1)
                    break

        if all_placed(board, n):
            print n
            print_board(board, n)
            sys.exit()

print -1



