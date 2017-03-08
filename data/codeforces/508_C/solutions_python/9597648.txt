__author__ = 'default'
def TaskC():
    import sys
    m, t, r = list(map(int,raw_input().split()))
    rdl1 = list(map(int,raw_input().split()))
    used = 0
    mas = [0]*r
    if r > t:
        print(-1)
        sys.exit()
    for i in range(len(rdl1)):
            if rdl1[i]+1 < mas[0]:
                pass
            else:
                for j in range(len(mas)):
                    if mas[j] < rdl1[i]+1:
                        mas[j] = rdl1[i]-j+t
                        used += 1
                        
                    else: break 
                mas.sort()
                
                    
    print(used)
TaskC()