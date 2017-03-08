#include <iostream>
#include <algorithm>
#include <vector>
#include <cstring>

using namespace std;

const int INF = 1000000000;

int N, M, K;
int A[105][105];

int main()
{
	cin >> N >> M >> K;
	for(int i = 0; i < N; i++) for(int j = 0; j < M; j++) cin >> A[i][j];

	int best = INF;
	if(N <= 10)
	{
		for(int b = 0; b < (1 << N); b++) // first column
		{
			int total = 0;
			for(int c = 0; c < M; c++)
			{
				int cur = 0;
				for(int r = 0; r < N; r++)
				{
					if(!(b & (1 << r)) != A[r][c]) cur++;
				}
				total += min(cur, N - cur);
			}

			best = min(best, total);
		}
	}
	else
	{
		for(int fr = 0; fr < N; fr++)
		{
			int total = 0;
			for(int r = 0; r < N; r++)
			{
				int cur = 0;
				for(int c = 0; c < M; c++)
				{
					if(A[fr][c] != A[r][c]) cur++;
				}
				total += min(cur, M - cur);
			}

			best = min(best, total);
		}
	}
	cout << (best <= K ? best : -1) << endl;
	return 0;
}
