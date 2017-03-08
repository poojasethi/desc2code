for i in range(input()):
    NK = map(int, raw_input().split())
    strings = map(str, raw_input().split())
    phrases = []
    for j in range(NK[1]):
        phrases.append(map(str, raw_input().split()))
    for j in strings:
        out = "NO"
        for k in phrases:
            if j in k: 
                out = "YES"
                break
        print out,