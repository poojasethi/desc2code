// Problem Link : http://www.codechef.com/MAY12/problems/MEDIAN
#include <map>
#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

map<int, int> R;

int solve(int N, int mask);

int main()
{
	int T, N;
	scanf("%d", &T);
	

	for(int i = 0; i < T; i++)
		{
			R.clear();
			scanf("%d", &N);
			
			int A[N], max = 0, mask=0;
			for(int j = 0; j < N; j++)
				{
					scanf("%d", A + j);
					if(max < A[j]) max = A[j];
				}
			
			for(int j = 0; j < N; j++)
				if(A[j] == max) mask += (1 << j);
			
			cout << solve(N, mask) << endl;
		}

	return 0;
}
			
int solve(int N, int mask)
{
	int c1 = 0, c0 = 0;
	//cerr << mask << endl;
	
	for(int i = 0; i < N; i++)
		if(mask & (1 << i)) c1++;
		else c0++;
	
	//cerr << c1 << " " << c0 << endl;
	
	if(c0 == 0) return 0;
	else if(c1 >= c0) return 1;
	else if(R.find(mask) != R.end()) return R[mask];
	
	int steps = 1<<10;
	for(int i = 0; i < N; i++)
		{
			c1 = c0 = 0;
			int to = -1;
			int go = mask;
			
			for(int j = i; j < N; j++)
				{
					if(mask & (1 << j)) c1++;
					else
						{
							go += (1 << j);
							c0++;
						}
					
					if(c1 >= c0 && go != mask)
						to = go;
				}
			
			if(to != -1) 
				steps = min(steps, solve(N, to) + 1);
		}
	R[mask] = steps;
	//cerr << mask << " " << steps << endl;
	return steps;
}
