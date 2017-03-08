#include <bits/stdc++.h>

using namespace std;

int N, R, a, b, x, y;

int main(){
	a = 0;
	b = 1000000;
	scanf("%d %d", &N, &R);
	for (int i = 0; i < R; i++){

		scanf("%d %d", &x, &y);
		if (x > y)
			swap(x, y);
		a = max(a, x);
		b = min(b, y);
	}

	if(R)
		printf("%d\n", (b - a > 0 ? b - a : 0));
	else
		printf("%d\n", N-1);

}
