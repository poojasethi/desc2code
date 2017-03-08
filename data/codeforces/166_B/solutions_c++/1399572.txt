#include <stdbool.h>
#include <stdio.h>

typedef struct vector vector;
struct vector { long long x, y; };

typedef struct point point;
struct point { int x, y; };

long long cross(vector v, vector u) {
	return v.x*u.y - u.x*v.y;
}

vector sub(point p, point q) {
	return (vector){q.x-p.x, q.y-p.y};
}

long long cmp(point p, point q, point r) {
	return cross(sub(p, q), sub(p, r));
}

void scan(point *p) {
	scanf("%d%d", &p->x, &p->y);
}

int main() {
	int n; scanf("%d", &n);
	point ps[100000];
	for (point *p = ps; p != ps+n; p++)
		scan(p);

	int m; scanf("%d", &m);
	for (int i = 0; i < m; i++) {
		point p; scan(&p);

		if (!(cmp(ps[0], ps[1], p) < 0 && cmp(ps[0], ps[n-1], p) > 0)) {
			puts("NO");
			return 0;
		}

		int l = 1, r = n-2;
		while (l < r) {
			int m = (l+r+1)/2;
			if (cmp(ps[0], ps[m], p) <= 0)
				l = m;
			else
				r = m-1;
		}

		if (!(cmp(ps[0], ps[l], p) <= 0 &&
				cmp(ps[0], ps[l+1], p) >= 0 &&
				cmp(ps[l], ps[l+1], p) < 0)) {
			puts("NO");
			return 0;
		}
	}

	puts("YES");
	return 0;
}
