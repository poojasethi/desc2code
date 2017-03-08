#-------------------------------------------------------------------------------
# Name:        B. Multi-core Processor
# Purpose:     Only for Contest purpose
#
# Author:      Md. Khairullah Gaurab
#
# Created:     15/04/2014
# Copyright:   (c) Md. Khairullah Gaurab
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from __future__ import print_function
def main():
    n, m, k = map(int,raw_input().split())
    ins = [[0]*(m) for i in xrange(n+1)]
    cell = [False]*(k+1)
    nn = [0]*(k+1)
    core = [0]*(n+1)
    for i in xrange(n):
        ins[i+1] = map(int,raw_input().split())
    for i in xrange(m):
        for j in xrange(1,k+1):
            nn[j] = 0
        for j in xrange(1,n+1):
            if core[j]==0:
                d = ins[j][i]
                if d!=0:
                    if cell[d]:
                        core[j] = i + 1
                    elif nn[d]!=0:
                        cell[d] = True
                        core[j] = core[nn[d]] = i + 1
                        nn[d] = j
                    elif nn[d]==0:
                        nn[d] = j

    for i in xrange(1,n+1):
        print(core[i])
if __name__ == '__main__':
    main()
