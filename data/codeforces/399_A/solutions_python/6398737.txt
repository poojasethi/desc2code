# Author: peihong

def solve(n, p, k):
    return [x for x in range(max(1,p-k), min(p+k,n)+1)]

if __name__ == '__main__':
    n, p, k = map(int, raw_input().split())

    pages = solve(n, p, k)

    left = ''
    right = ''
    if not 1 in pages:
        print '<<',

    for x in pages:
        if x == p:
            print '(%d)' % x,
        else:
            print x,
        
    if not n in pages:
        print '>>'
