for _ in range(input()):
    n = input()
    ans = (n*(n+1))/2
    ans -= 2 ;
    i = 2
    while(i <= n):
        ans -= 2*i
        i = i* 2
    print ans 
