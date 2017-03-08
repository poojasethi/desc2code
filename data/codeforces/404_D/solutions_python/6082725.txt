# zero, one_used, one_unused, two, mine
t = None

line = raw_input()

big_prime = 1000000007

for c in line:
    if t is None:
        zero = 1
        one_used = 0
        one_unused = 1
        two = 0
        mine = 1
    else:
        zero = (t[0] + t[1]) % big_prime
        one_used = t[4]
        one_unused = (t[0] + t[1]) % big_prime
        two = t[4]
        mine = (t[2] + t[3] + t[4]) % big_prime

    if c == '0':
        t = (zero, 0, 0, 0, 0)
    if c == '1':
        t = (0, one_used, one_unused, 0, 0)
    if c == '2':
        t = (0, 0, 0, two, 0)
    if c == '*':
        t = (0, 0, 0, 0, mine)
    if c == '?':
        t = (zero, one_used, one_unused, two, mine)
    # print t

print (t[0] + t[1] + t[4]) % big_prime

