#include <iostream>
#include <cstring>
#include <cmath>
#include <cstdio>

using namespace std;

double table[2][1005];

int main()
{
	int N, K;
	cin >> N >> K;
	for(int t = 1; t <= N; t++)
	{
		for(int l = 1; l < 1000; l++)
		{
			double good = ((l + table[(t - 1) & 1][l + 1]) + l * ((l + 1) / 2.0 + table[(t - 1) & 1][l])) / (l + 1);
			table[t & 1][l] = (good + (K - 1.0) * table[(t - 1) & 1][l]) / K;
		}
		double good = (1000 + 2) / 2.0 + table[(t - 1) & 1][1000];
		table[t & 1][1000] = (good + (K - 1.0) * table[(t - 1) & 1][1000]) / K;
	}
	printf("%.12f\n", K * table[N & 1][1]);
}
