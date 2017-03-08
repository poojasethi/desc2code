#include <cstdio>
#include <algorithm>
using namespace std;

int findFloor(int v, int unit)
{
	if(v < 0) return v/unit;
	return v/unit+1;
}

int main()
{
	int A, B, x1, y1, x2, y2, ans1, ans2;
	scanf("%d%d%d%d%d%d", &A, &B, &x1, &y1, &x2, &y2);
	
	ans1 = abs( findFloor(x1+y1, 2*A) - findFloor(x2+y2, 2*A) );
	ans2 = abs( findFloor(x1-y1, 2*B) - findFloor(x2-y2, 2*B) );
	
	printf("%d\n", max(ans1, ans2));
	return 0;
}