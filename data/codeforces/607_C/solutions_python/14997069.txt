import os

def main_entry():
    c2i = {'N':0, 'S':1, 'W':2, 'E':3}
    while True:
        try:
            n = int(raw_input())
        except ValueError:
            continue
        except EOFError:
            break
        a = str(raw_input())[::-1]
        b = str(raw_input())
        c = ''
        for k in a:
            c += str(c2i[k]^1)
        c += '#'
        for k in b:
            c += str(c2i[k])
        n = len(c)
        f = [-1 for i in xrange(n)]
        for i in range(1, n):
            k = f[i-1]
            while k>=0 and c[i]!=c[k+1]:
                k = f[k]
            if c[i]==c[k+1]:
                f[i] = k+1
        if f[n-1]==-1:
            print 'YES'
        else:
            print 'NO'

if __name__ == '__main__':
    main_entry()
