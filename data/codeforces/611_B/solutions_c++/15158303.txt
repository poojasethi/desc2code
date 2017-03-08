#include<bits/stdc++.h>
using namespace std;
int main()
{
	long long int a,b;
	cin>>a>>b;
	int c = 0;
	for(int i = 0; (1LL << i) / 2 <= b; ++i)
		for(int j = 0; j <= i - 2; ++j) {
			long long x = (1LL << i) - 1 - (1LL << j);
			c += a <= x && x <= b;
		}
	printf("%d\n", c);
	return 0;
}

