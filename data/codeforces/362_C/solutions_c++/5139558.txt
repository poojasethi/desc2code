#include<cstdio>
using namespace std;

#define MAX 5010
#define INF 1e9

int bigger[MAX][MAX], v[MAX];

int main()
{
	int n, total = 0;

	scanf("%d", &n);
	for(int i=0; i<n; ++i) scanf("%d", &v[i]);
	
	for(int i=0; i<n; ++i)
	{
		bigger[i][i] = 0;
		for(int j=i+1; j<n; ++j) bigger[i][j] = bigger[i][j-1] + ((v[j] > v[i]) ? 1 : 0);
		for(int j=i-1; j>=0; --j) bigger[i][j] = bigger[i][j+1] + ((v[j] > v[i]) ? 1 : 0);
		total += bigger[i][0];
	}
	
	int count = 0, ntotal = INF;
	for(int i=0; i<n; ++i)
		for(int j=i+1; j<n; ++j)
			if(v[i] > v[j])
			{
				int auxtotal = total + bigger[i][j-1] - bigger[j][i+1] - (j-i-bigger[i][j-1]) + (j-i-bigger[j][i+1]) - 1;
				if(auxtotal == ntotal) count++;
				else if(auxtotal < ntotal) ntotal = auxtotal, count = 1;
			}
	printf("%d %d\n", ntotal, count);
}
