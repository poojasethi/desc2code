import sys
import math


def get_exc(s):
    return s.split('(')[1].split(',')[0].strip()


def get_alert(s):
    return s.split('"')[1]

def solve(data, exception):
    counter = 0
    for x in data:
        if x == 'try':
            counter += 1
        elif x.startswith('catch'):
            exc = get_exc(x)
            if exc == exception and not counter:
                return get_alert(x)
            counter = max(0, counter - 1)
    return 'Unhandled Exception'

if __name__ == '__main__':
    sys.stdin.readline()
    data = []
    exception = None
    for s in sys.stdin.readlines():
        s = s.replace('\n', '').strip()
        
        if s.startswith('throw'):
            exception = s.split('(')[1].split(')')[0].strip()
            continue
        if not exception:
            continue
        
        data.append(s)
        
    sys.stdout.write(str(solve(data, exception)))