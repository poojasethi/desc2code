for _ in range(input()):
    n , k = map(int , raw_input().split())
    ans = 0 
    arr = map(int, raw_input().split())
    for i in arr:
        if ((i+k) % 7 == 0 ):
            ans += 1 
    print ans
