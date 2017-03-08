#include <iostream>
#include <vector>
#include <stdio.h>
#include <algorithm>
#include <cmath>
using namespace std;

typedef std::pair<long double, long double> intPair;

intPair median(vector<long double> v)
{
	sort(v.begin(), v.end());
	long long int l = v.size();
	intPair p;
	p.first = v[(l-1)/2];
	p.second = v[(l/2)];

	// cout << "p.first is " << p.first << endl;
	// cout << "p.second is " << p.second << endl;
	return p;
}

int main(int argc, char const *argv[])
{
	int testcases;
	cin >> testcases;
	for (int j = 0; j < testcases; ++j)
	{
		int N;
		cin >> N;
		vector<long double> X(N), Y(N);
		if (N==0)
		{
			cout << "0" << endl;
			continue;
		}
		for (int i = 0; i < N; ++i)
		{
			cin >> X[i];
			cin >> Y[i];
		}

		intPair Xmed = median(X);
		intPair Ymed = median(Y);

		long n1,n2;

		n1 = floor(Xmed.second) - ceil(Xmed.first) + 1;
		n2 = floor(Ymed.second) - ceil(Ymed.first) + 1;

		long long ans = 1ll*n1*n2;

		printf("%lld\n", ans);

	}
	
	return 0;
}