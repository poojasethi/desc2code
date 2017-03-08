
import sys
tt = int(raw_input())
for i in xrange(0, tt+1, 1234567):
    for j in xrange(0, tt - i + 1, 123456):
        if (tt - i - j) % 1234 == 0:
            print 'YES'
            sys.exit()

print 'NO'
sys.exit()