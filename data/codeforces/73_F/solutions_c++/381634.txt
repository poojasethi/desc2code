#include <cstdio>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;
#define x first
#define y second
typedef double dbl;

typedef pair <dbl, dbl> pnt;

pnt operator - (pnt a, pnt b) {
  return pnt (a.x - b.x, a.y - b.y);
}

pnt st, dir;
dbl _w, _s, _len;

inline dbl f(dbl t) { 
  dbl x = st.x + dir.x * t,
      y = st.y + dir.y * t;
  dbl r = atan2 (y, x) - _s;
  while (r < 0) {
    r += 2 * M_PI;
  }
  while (r > 2 * M_PI) {
    r -= 2 * M_PI;
  }
//  fprintf (stderr,  "%lf : %lf (%lf %lf) | %lf\n", _len * t * _w, min(r, 2 * M_PI - r), x, y, r);
  return _len * t * _w / min(r, 2 * M_PI - r);
}

dbl get (pnt a, pnt b, dbl s, dbl w) {
  st = a;
  dir = b - a;
  _s = s;
  _w = w;
  _len = hypot (dir.x, dir.y);

  dbl res = 0;
  for (int i = 0; i <= 100; i++) {
    dbl t = f (i / 100.);
    if (t > res) {
      res = t;
    }
  }
  return res;
}

void read (pnt &p) {
  double x, y;
  scanf ("%lf%lf", &x, &y);
  p.x = x;
  p.y = y;
}

int main (void) {
  pnt a, b;
  read(a);
  read(b);
  
  int n;
  scanf ("%d", &n);

  vector <dbl> v(1, 0);
  for (int i = 0; i < n; i++) {
    pnt p;
    read(p);
    double s, w;
    scanf("%lf%lf", &s, &w);
    v.push_back(get(a - p, b - p, s, w));
  }

  sort (v.begin(), v.end());
  reverse (v.begin(), v.end());
  int k;
  scanf ("%d", &k);
  printf ("%.20lf\n", v[k]);
  
  return 0;
}