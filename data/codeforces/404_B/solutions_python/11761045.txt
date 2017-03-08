""" 
    Author: Hemanth Kumar Veeranki
    Handle:harry7

"""
#!/usr/bin/python
a,d=map(float,raw_input().split())
n=input()
for i in range(1,n+1):
    s=(d*i)%(4*a)
    if s<=a:
        print s,0
    elif s<=2*a:
        print a,s-a
    elif s<=3*a:
        print 3*a-s,a
    else:
        print 0,4*a-s
