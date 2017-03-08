
if __name__ == '__main__':

    n,m = map(int,raw_input().split())
    points= map(int,raw_input().split())
    colors = len(points)* [-1]
    color = 0
    points = sorted(enumerate(points),key=lambda x:x[1])

    for i,p in points:
        colors[i] = color
        color = 0 if color == 1 else 1

    print ' '.join(map(str,colors))

