#!/usr/bin/env python
[a, b] = map(int, raw_input().split())
[c, d] = map(int, raw_input().split())
[A, B] = map(int, raw_input().split())
[C, D] = map(int, raw_input().split())
if (((a > max(B, D)) & (d > max(A, C))) | ((c > max(B, D)) & (b > max(A, C)))):
    print "Team 1"
else:
    if ((((A > b) & (D > c)) | ((C > b) & (B > c))) & (((A > d) & (D > a)) | ((C > d) & (B > a)))):
        print "Team 2"
    else:
        print "Draw"
