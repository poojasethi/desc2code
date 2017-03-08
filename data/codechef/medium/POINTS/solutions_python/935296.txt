"""
 Problem: The Way to a Friends House is Never Too Long
 URL: http://www.codechef.com/problems/POINTS

 Complexity: O(n*log(n) + kn) where k is the cost of a distance calculation

"""

__author__ = "Ronald Andreu Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


import math
n = int(raw_input())

for i in range(n):
    raw_input()
    np = int(raw_input())

    points = []
    for i in range(np):
        points.append(map(int, raw_input().split()))

    points = sorted(points, key=lambda x: x[0] + 1.0/(1+x[1])) # <- proud of this trick =)
    total = 0
    for i in range(np-1):
        total += math.sqrt((points[i][0] - points[i+1][0])**2 + (points[i][1] - points[i+1][1])**2)
    print "%.2f" % total
    

