
def main():
    n = int(raw_input())
    s = list(raw_input())
    w = list(raw_input())

    maior = menor = igual = 1
    possibilidades = 1

    for i in xrange(n):
        if s[i] != "?" and w[i] != "?":
            if int(s[i]) > int(w[i]):
                maior = 0
                igual = 0
            elif int(s[i]) < int(w[i]):
                menor = 0
                igual = 0
        elif s[i] != "?":
            maior *= 10 - int(s[i])
            menor *= int(s[i]) + 1
            possibilidades *= 10
        elif w[i] != "?":
            maior *= int(w[i]) + 1
            menor *= 10 - int(w[i])
            possibilidades *= 10
        else:
            maior *= 55
            menor *= 55
            igual *= 10
            possibilidades *= 100
        maior = maior % 1000000007
        menor = menor % 1000000007
        igual = igual % 1000000007
        possibilidades = possibilidades % 1000000007

    print (possibilidades - maior - menor + igual) % 1000000007

if __name__ == '__main__':
    main()