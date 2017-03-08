n = int(input())
vis_x, vis_y = [0]*100002, [0]*100002
x, y = [0]*n, [0]*n
for i in xrange(n):
  xx, yy = map(int, raw_input().split())
  x[i], y[i] = xx, yy;
  vis_x[xx] += 1;
  vis_y[yy] += 1;
for i in xrange(n):
  print (n-1)+vis_x[y[i]], (n-1)-vis_x[y[i]];
