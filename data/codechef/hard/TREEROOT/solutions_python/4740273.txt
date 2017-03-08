T = int(raw_input())
for i in range (0,T):
    N = int(raw_input())
    sum_x = 0
    sum_y = 0
    for j in range (0,N):
        x,y = raw_input().split()
        #print "id:{},sum_child:{}".format(x,y)
        sum_x += int(x)
        sum_y += int(y)
    print sum_x-sum_y




