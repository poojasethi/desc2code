n, k = map(int, raw_input().split())

grid = [['S' for i in range(n)] for j in range(n)]

def main(grid):
    ctr = 0
    for i in range(n):
        if ctr >= k: 
            break
        even = i % 2
        for j in range(n):
            if ctr >= k:
                break
            if even:
                if j % 2 != 0:
                    grid[i][j] = 'L'
                    ctr += 1
            else:
                if j % 2 == 0:
                    grid[i][j] = 'L'
                    ctr += 1
    if ctr < k:
        print "NO"
    else:
        print "YES"
        for row in grid:
            print "".join(row)


main(grid)