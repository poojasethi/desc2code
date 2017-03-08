for i in range(input()):
    j=input()
    a=map(int,raw_input().split())
    b=[int(a[j]/(j+1)) for j in range(len(a))]
    if sum(b)%2==0:
        print "BOB"
    else:
         print "ALICE"