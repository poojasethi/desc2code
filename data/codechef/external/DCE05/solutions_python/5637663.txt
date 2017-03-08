from math import floor
from math import log

n = int(raw_input());

while n > 0:
    no = int(raw_input());
    print int(2**floor(log(no, 2)));
    n -= 1;
