from sys import stdin, stdout
def main():
    m, n = map(int, stdin.readline().split())
    k = [0] * 3
    for b in stdin.read().split():
        if b == '11':
            k[0] += 1
        elif b == '00':
            k[2] += 1
        else:
            k[1] += 1
    rest = [k[0] % n, k[1] % (2 * n), k[2] % n]
    if rest[0] + rest[1] + rest[2]:
        if rest[0] + rest[1] + rest[2] <= n:
            stdout.write(' '.join(['11'] * rest[0] + ['10'] * rest[1] + ['00'] * rest[2]))
            stdout.write('\n')
        else:
            l0 = ['10'] * (rest[1] - rest[1] / 2)
            l1 = ['01'] * (rest[1] / 2)
            for l in (l0, l1):
                while rest[0] and len(l) < n:
                    l.append('11')
                    rest[0] -= 1
            for l in (l0, l1):
                while rest[2] and len(l) < n:
                    l.append('00')
                    rest[2] -= 1
            l2 = ['11'] * rest[0] + ['00'] * rest[2]
            stdout.write('\n'.join(' '.join(l) for l in (l0, l1, l2) if l))
            stdout.write('\n')
    b = [('11', k[0] / n), ('10', k[1] / (2 * n)), ('01', k[1] / (2 * n)), ('00', k[2] / n)]
    stdout.write('\n'.join('\n'.join(' '.join(s for i in xrange(n)) for j in xrange(rep)) for s, rep in b if rep))
main()
