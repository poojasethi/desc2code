from math import factorial as fac
def catalan(n):
    return fac(2*n) // fac(n+1) // fac(n)
 
def num_handshakes(n):
    if n % 2 == 1: return 0
    return catalan(n//2)
T=int(raw_input())
while T>0:
    N=int(raw_input())
    print num_handshakes(2*N) %100003
    T=T-1