from collections import deque

x1, y1, x2, y2 = map(int, raw_input().split());

n = input();
vol = set();
for i in xrange(n):
    r, c1, c2 = map(int, raw_input().split());
    for j in xrange(c1,c2+1):
        vol.add((r, j));

dq = deque( [(x1, y1, 0)] );
pop = dq.popleft;
pb = dq.append;

while dq:
        x, y, z = pop();
        for i in xrange(-1, 2):
            for j in xrange(-1, 2):
                nx = x + i;
                ny = y + j;
                if (nx, ny) in vol:
                    vol.remove((nx, ny));
                    pb((nx, ny, z + 1));
                if nx == x2 and ny == y2:
                    print(z + 1);
                    exit(0);
print(-1);
                
    
