def sol():
    lower, upper = map(int, raw_input().split())
    res = 0
    for val in range(1, 10):
        if lower <= val <= upper: res+=1 
    for length in range(2, 19):
        for startend in range(1, 10):
            alreadyval = startend * pow(10, length - 1) + (0 if length == 1 else startend)
            smallestpos = max(0, (lower - alreadyval + 9) / 10)
            largestpos = min(pow(10, length - 2) - 1, (upper - alreadyval) / 10)
            res += max(0, largestpos - smallestpos + 1)
    print(res)
sol()