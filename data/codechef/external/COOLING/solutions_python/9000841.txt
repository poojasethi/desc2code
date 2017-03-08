import sys
T = raw_input()
cnt = 0
for i in range(0,int(T)):
    cnt = 0
    k = 0
    N = raw_input()
    piweight = map(int,sys.stdin.readline().split()) 
    capacity = map(int,sys.stdin.readline().split()) 
  
    piweight.sort()
    capacity.sort()
    for j in range(len(capacity)):
        if piweight[k] > capacity[j]:
            continue
        cnt += 1
        k += 1
    print cnt
        
    