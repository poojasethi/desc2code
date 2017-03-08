#include <stdio.h>

typedef struct pair pair;
struct pair { int l, r; };

int main() {
	int n; scanf("%d", &n);

	int s[100000], sn = 0, a = 0;
	pair ps[100000]; int pn = 0;
	for (int i = 0; i < n; i++) {
		int b; scanf("%d", &b);

		if (b > a)
			for (int j = a+1; j <= b; j++)
				s[sn++] = i;
		else if (b < a)
			for (int j = b+1; j <= a; j++)
				ps[pn++] = (pair){s[--sn], i-1};

		a = b;
	}

	for (int j = 1; j <= a; j++) 
		ps[pn++] = (pair){s[--sn], n-1};

	printf("%d\n", pn);
	for (pair *p = ps; p != ps+pn; p++)
		printf("%d %d\n", p->l + 1, p->r + 1);

	return 0;
}
