import sys

def main() :
    lines = sys.stdin.readlines()
    cases = int(lines[0])
    count = 1
    for case in xrange(cases) :
        n, msg = lines[count].split()
        count = count + 1
        n = int(n)
        num = 2 ** n
        output = ['a']*(num)
        for i in xrange(num) :
            temp = i
            revbin = 0
            for j in xrange(n) :
                revbin = revbin * 2 + temp % 2
                temp = temp / 2
            output[revbin] = msg[i]
        print "".join(output)

main()