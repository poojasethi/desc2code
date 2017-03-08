
def main():
    inicio = raw_input()
    fim = raw_input()
    k = int(raw_input())

    vA = [-1]*(k+1)
    vB = [-1]*(k+1)

    if inicio == fim and k == 0:
        return 1
    else:
        A = B = 0

        if inicio != fim:
            vA[0] = 0
            vB[0] = 1
        else:
            vA[0] = 1
            vB[0] = 0

        for i in xrange(len(inicio)):
            atual = inicio[i:]+inicio[:i]
            if atual == fim:
                A += 1
            else:
                B += 1

        for n in xrange(1, k+1):
            vA[n] = (vA[n-1]*(A-1) + vB[n-1]*A)%1000000007
            vB[n] = (vA[n-1]*B     + vB[n-1]*(B-1))%1000000007

        return vA[k]

if __name__ == '__main__':
    print main()