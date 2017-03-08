a = input()
for x in range(a):
    n = input()
    string = str(n**0.5)
    i=0
    wow = ''
    while string[i] != '.':
        wow += string[i]
        i += 1
    print wow
