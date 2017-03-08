#include <stdio.h>

typedef struct { int p, m, cp, cm; } vertex;
vertex vs[1000000];

int main() {
	int n, m; scanf("%d%d", &n, &m);

	int a[n];
	for (int i = 0; i < n; i++) {
		scanf("%d", &a[i]);
		if (a[i] > 0)
			vs[a[i]-1].p++;
		else
			vs[-a[i]-1].m++;
	}

	int tm = 0;
	for (int i = 0; i < n; i++)
		tm += vs[i].m;

	int tcm = 0;
	for (int i = 0; i < n; i++)
		if (tm - vs[i].m + vs[i].p == m) {
			tcm++;
			vs[i].cm--;
			vs[i].cp++;
		}

	for (int i = 0; i < n; i++) {
		int j = a[i] > 0 ? a[i]-1 : -a[i]-1;
		int cm = tcm + vs[j].cm, cp = vs[j].cp;
		if (cm && cp)
			puts("Not defined");
		else if (cm && a[i] < 0 || cp && a[i] > 0)
			puts("Truth");
		else
			puts("Lie");
	}

	return 0;
}
