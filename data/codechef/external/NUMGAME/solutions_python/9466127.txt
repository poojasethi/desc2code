turn = "ALICE"

t = int(raw_input())
for i in range(t):
    x = int(raw_input())
    if x % 2 == 0:
        print 'ALICE'
    else:
        print 'BOB'
